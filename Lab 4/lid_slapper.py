import threading
import time
from pathlib import Path

import board
import busio
import adafruit_mpr121
import numpy as np
import pi_servo_hat
import sounddevice as sd
from piper import PiperVoice

# Don't Touch Lid Slapper
# A cookie jar with copper tape on its lid. The tape is wired to the MPR121
# capacitive sensor. Touch the lid and a cardboard arm on the servo slaps
# your hand away while the jar yells at you through the USB speaker.
# Keep trying and the jar gets angrier:
#   1st touch  -> warning wiggle ("I see you...")
#   2nd touch  -> one slap
#   3rd+ touch -> double slap
# If nobody touches the lid for CALM_DOWN seconds, the jar forgives you.
#
# Optional: a Qwiic proximity sensor at the rim (hand entering the jar).
# The script runs fine without it.

# --- Capacitive sensor ---
LID_PAD = 0             # MPR121 pad the copper tape is wired to

# --- Servo ---
SERVO_CH = 0
SERVO_HOME = 20         # arm resting, tucked against the jar
SERVO_SLAP = 110        # arm swung out over the lid
WIGGLE_LOW = 25
WIGGLE_HIGH = 45

# --- Timing ---
CALM_DOWN = 10          # seconds with no touches before anger resets
COOLDOWN = 1.0          # seconds after a reaction before reacting again

# --- Optional proximity sensor ---
# Higher values = closer. Run qwiic_distance.py to calibrate with and without
# a hand (and with the cookies in the jar!).
HAND_THRESHOLD = 150

# --- Voice (Piper TTS, same voice as Lab 3) ---
VOICE_PATH = Path(__file__).resolve().parent.parent / "Lab 3" / "voices" / "en_US-lessac-medium.onnx"
# None = system default output. If the USB speaker isn't the default, run
# `python -m sounddevice` to list devices and put its number or name here.
SPEAKER_DEVICE = None


class Speaker:
    """Piper TTS played through the USB speaker, same as Lab 3's echo_bot.py."""

    def __init__(self, voice_path):
        self.voice = PiperVoice.load(str(voice_path))
        self.thread = None

    def _speak(self, text):
        for chunk in self.voice.synthesize(text):
            audio = np.frombuffer(chunk.audio_int16_bytes, dtype=np.int16)
            sd.play(audio, samplerate=chunk.sample_rate, device=SPEAKER_DEVICE)
            sd.wait()

    def say(self, text):
        # Speak in the background so the servo can move at the same time.
        self.wait()
        self.thread = threading.Thread(target=self._speak, args=(text,))
        self.thread.start()

    def wait(self):
        if self.thread is not None:
            self.thread.join()


# --- Set up capacitive sensor ---
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

# --- Set up servo ---
servo = pi_servo_hat.PiServoHat()
servo.restart()
servo.move_servo_position(SERVO_CH, SERVO_HOME)

# --- Set up voice ---
if not VOICE_PATH.is_file():
    raise RuntimeError(f"Piper voice not found at {VOICE_PATH}. Run Lab 3's setup.sh first.")
speaker = Speaker(VOICE_PATH)

# --- Optional proximity sensor ---
proximity_sensor = None
try:
    import qwiic_proximity
    sensor = qwiic_proximity.QwiicProximity()
    if sensor.connected:
        sensor.begin()
        proximity_sensor = sensor
        print("Proximity sensor found.")
except Exception:
    pass


def wiggle():
    for _ in range(3):
        servo.move_servo_position(SERVO_CH, WIGGLE_HIGH)
        time.sleep(0.12)
        servo.move_servo_position(SERVO_CH, WIGGLE_LOW)
        time.sleep(0.12)
    servo.move_servo_position(SERVO_CH, SERVO_HOME)


def slap():
    # Swing out fast, pause so the hit lands, then return slower.
    servo.move_servo_position(SERVO_CH, SERVO_SLAP)
    time.sleep(0.25)
    for angle in range(SERVO_SLAP, SERVO_HOME - 1, -5):
        servo.move_servo_position(SERVO_CH, angle)
        time.sleep(0.02)


def react(anger):
    if anger == 1:
        speaker.say("I see you. Put it down.")
        wiggle()
    elif anger == 2:
        speaker.say("I said no! Slap!")
        slap()
    else:
        speaker.say("Cookie police! Slap slap!")
        slap()
        slap()
    speaker.wait()


def hand_in_jar():
    if proximity_sensor is None:
        return False
    return proximity_sensor.get_proximity() > HAND_THRESHOLD


anger = 0
last_touch = 0
was_touched = False

print("Lid Slapper ready! Touch the lid. Ctrl+C to quit.")
speaker.say("Just a normal cookie jar.")

try:
    while True:
        touched = mpr121[LID_PAD].value or hand_in_jar()
        now = time.time()

        if anger > 0 and now - last_touch > CALM_DOWN:
            anger = 0
            speaker.say("Just a normal cookie jar.")

        # React on the rising edge of a touch, not every loop while held.
        if touched and not was_touched:
            anger += 1
            last_touch = now
            react(anger)
            time.sleep(COOLDOWN)
            touched = mpr121[LID_PAD].value or hand_in_jar()

        was_touched = touched
        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nStopping Lid Slapper.")
    servo.move_servo_position(SERVO_CH, SERVO_HOME)
