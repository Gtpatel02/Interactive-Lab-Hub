# Ph-UI!!!

<details>
	<summary><strong>Instructions for Students (Click to Expand)</strong></summary>
  
	**Submission Cleanup Reminder:**
	- This README.md contains extra instructional text for guidance.
	- Before submitting, remove all instructional text and example prompts from this file.
	- You may delete these sections or use the toggle/hide feature in VS Code to collapse them for a cleaner look.
	- Your final submission should be neat, focused on your own work, and easy to read for grading.
  
	This helps ensure your README.md is clear, professional, and uniquely yours!
</details>

---

---

## Lab Overview
Team: <canvas group name>  
Members: Full Name (netid, github-handle), ...  
Clock name: <name>


For lab this week, we focus on both sensing and actuation, bringing new modes of input and output into your devices, while also prototyping the physical structure and overall look of the device. You will consider how the physical form supports sensing and actuation, and how these elements come together to shape the interaction and aesthetics of the device.

---

## Lab Structure

A) [Capacitive Sensing](#part-a)

B) [More Sensors](#part-b)

C) [Servo Actuation](#part-c)

D) [Physical Interaction Design: Feast Automata](#part-d)

E) [Build & Integrate](#part-e)

F) [Final Documentation](#part-f)

---

### Part A
### Capacitive Sensing, a.k.a. Human-Twizzler Interaction

<img width="1488" height="518" alt="image" src="https://github.com/user-attachments/assets/67af0ca1-4aae-4ea2-8956-a044afdf4651" />

---

### Part B
### More sensors

#### Light/Proximity/Gesture sensor (APDS-9960)

We here want you to get to know this awesome sensor [Adafruit APDS-9960](https://www.adafruit.com/product/3595). It is capable of sensing proximity, light (also RGB), and gesture! 
 
<img src="https://cdn-shop.adafruit.com/970x728/3595-06.jpg" width=200>
 

Connect it to your pi with Qwiic connector and try running the three example scripts individually to see what the sensor is capable of doing!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python proximity_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python gesture_test.py
...
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python color_test.py
...
```

You can go the the [Adafruit GitHub Page](https://github.com/adafruit/Adafruit_CircuitPython_APDS9960) to see more examples for this sensor!

#### Rotary Encoder 

A rotary encoder is an electro-mechanical device that converts the angular position to analog or digital output signals. The [Adafruit rotary encoder](https://www.adafruit.com/product/4991#technical-details) we ordered for you came with separate breakout board and encoder itself, that is, they will need to be soldered if you have not yet done so! We will be bringing the soldering station to the lab class for you to use, also, you can go to the MakerLAB to do the soldering off-class. Here is some [guidance on soldering](https://learn.adafruit.com/adafruit-guide-excellent-soldering/preparation) from Adafruit. When you first solder, get someone who has done it before (ideally in the MakerLAB environment). It is a good idea to review this material beforehand so you know what to look at.

<p float="left">

   
<img src="https://cdn-shop.adafruit.com/970x728/377-02.jpg" height="200" />
<img src="https://cdn-shop.adafruit.com/970x728/4991-09.jpg" height="200">
</p>

Connect it to your pi with Qwiic connector and try running the example script, it comes with an additional button which might be useful for your design!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python encoder_test.py
```

You can go to the [Adafruit Learn Page](https://learn.adafruit.com/adafruit-i2c-qt-rotary-encoder/python-circuitpython) to learn more about the sensor! The sensor actually comes with an LED (neo pixel): Can you try lighting it up? 

#### Joystick 


A [joystick](https://www.sparkfun.com/products/15168) can be used to sense and report the input of the stick for it pivoting angle or direction. It also comes with a button input!

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/5/8/15168-SparkFun_Qwiic_Joystick-01.jpg" height="200" />
</p>

Connect it to your pi with Qwiic connector and try running the example script to see what it can do!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python joystick_test.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Joystick_Py) to learn more about the sensor!

#### Distance Sensor


Earlier we have asked you to play with the proximity sensor, which is able to sense objects within a short distance. Here, we offer [Sparkfun Proximity Sensor Breakout](https://www.sparkfun.com/products/15177), With the ability to detect objects up to 20cm away.

<p float="left">
<img src="https://cdn.sparkfun.com//assets/parts/1/3/5/9/2/15177-SparkFun_Proximity_Sensor_Breakout_-_20cm__VCNL4040__Qwiic_-01.jpg" height="200" />

</p>

Connect it to your pi with Qwiic connector and try running the example script to see how it works!

```
(circuitpython) pi@ixe00:~/Interactive-Lab-Hub/Lab 4 $ python qwiic_distance.py
```

You can go to the [SparkFun GitHub Page](https://github.com/sparkfun/Qwiic_Proximity_Py) to learn more about the sensor and see other examples

---

### Part C
### Servo Actuation

Now that you have explored several forms of sensing, add physical output by learning to control a servo motor. Complete the Servo pHAT setup and basic servo test before beginning your interaction design.

### Servo Control with SparkFun Servo pHAT
For this lab, you will use the **SparkFun Servo pHAT** to control a micro servo (such as the Miuzei MS18 or similar 9g servo). The Servo pHAT stacks directly on top of the Adafruit Mini PiTFT (135×240) display without pin conflicts:
- The Mini PiTFT uses SPI (GPIO22, 23, 24, 25) for display and buttons ([SPI pinout](https://pinout.xyz/pinout/spi)).
- The Servo pHAT uses I²C (GPIO2 & 3) for the PCA9685 servo driver ([I2C pinout](https://pinout.xyz/pinout/i2c)).
- Since SPI and I²C are separate buses, you can use both boards together.
**⚡ Power:**
- Plug a USB-C cable into the Servo pHAT to provide enough current for the servos. The Pi itself should still be powered by its own USB-C supply. Do NOT power servos from the Pi’s 5V rail.

<p align="center">
    <img src="Servo_pHAT.gif" alt="Servo pHAT Demo" width="400"/>
</p>

**Basic Python Example:**
We provide a simple example script: `Lab 4/pi_servo_hat_test.py` (requires the `pi_servo_hat` Python package).
Run the example:
```
python pi_servo_hat_test.py
```
For more details and advanced usage, see the [official SparkFun Servo pHAT documentation](https://learn.sparkfun.com/tutorials/pi-servo-phat-v2-hookup-guide/all#resources-and-going-further).
A servo motor is a rotary actuator that allows for precise control of angular position. The position is set by the width of an electrical pulse (PWM). You can read [this Adafruit guide](https://learn.adafruit.com/adafruit-arduino-lesson-14-servo-motors/servo-motors) to learn more about how servos work.

---

### Part D
### Physical Interaction Design: Feast Automata

**\*\*\*Draw 5 sketches that explore different physical arrangements for your sensing and actuation.\*\*\***
<img width="3969" height="2341" alt="IMG_7786" src="https://github.com/user-attachments/assets/fbceceb5-767f-4540-95e8-13967917d578" />

**\*\*\*What questions do these sketches raise? What do you need to physically prototype to answer them?\*\*\***

#### Questions:
1. Can the capacitive sensor detect a touch through copper tape on a lid that’s handled constantly, or will normal jar handling cause false triggers?
2. Does the proximity sensor inside the rim reliably detect a hand entering the jar, or do the cookies themselves set it off?
3. Does the device need a base to keep it stable when the servo moves?
4. Should the jar react differently the more cookies someone takes, for example by escalating from a raised eyebrow to a slap?
5. At what distance should the face start “judging”? If it’s too sensitive, it reacts to people walking past; if it’s not sensitive enough, it reacts after the cookie is already gone.

#### What we physically prototype:
- Copper tape on the jar lid with the cap sensor
- Proximity sensor at the jar rim
- Cardboard arms of different lengths on the servo
- A cardboard base or housing for the electronics
- Cardboard faces and signs
- Physically move the prototype ourselves


**\*\*\*Pick one design to prototype and explain why.\*\*\***
We have decided to choose the first design, Don't Touch Lid Slapper.
We chose this because first off, the capacitive touch on the lid is the most direct trigger, since you have to touch the lid to open the jar. It is also pretty funny and it is very easy to see what it is trying to do, keep you healthier so you don't eat cookies. Also we can fit everything under the jar so it is easy to keep hidden and act like it's a normal jar even if it is not.

Build a cardboard or other low-fidelity physical prototype of your design.

**\*\*\*Document your rough prototype with photos and/or video.\*\*\***

---

## Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

---

### Part E

#### Build & Integrate: Sensing + Actuation

For Part 2, build the Feast Automata interaction you developed in Part D by connecting sensing/input to physical actuation.

**Your prototype should:**
- Use at least one sensing or input device.
- Use servo-based physical actuation.
- Connect sensing and actuation into a meaningful interaction around eating, drinking, cooking, serving, or sharing food.
- Additional inputs, displays, LEDs, buttons, or other outputs are optional extensions.

**Document your system with:**
- Code for your sensing + actuation prototype
- Photos and/or video of the working prototype in action
- A simple interaction diagram or sketch showing how sensing and actuation are connected
- Written reflection: What did you learn about connecting sensing, movement, and physical form? What was fun, surprising, or challenging?

**Questions to consider:**
- How does your chosen sensor or input shape the physical response?
We used capacitive touch through copper tape on the lid, so the jar only reacts when someone actually touches the lid. That’s the moment they’re about to take a cookie. Because the trigger is so direct, the response can be direct too: the arm slaps the hand that touched the lid. A touch either happens or it doesn’t, so the jar can’t tell how close someone is. That’s why we made it react to how many times you try instead of how close you get. The 1st touch gets a warning wiggle and “I see you. Put it down.” The 2nd gets one slap. The 3rd and after get a double slap and “Cookie police!” The code only counts a new touch, not a hand resting on the lid, so holding the lid doesn’t set off a string of slaps. The only issue we did have is that when we moved the sensor/jar, there seemed to be a response that was given but besides that it would only work when we touched the jar.
- How does the physical arrangement of the sensor and actuator change the interaction?
The copper tape is on the lid and the servo arm is mounted right next to it, so the slap lands where the hand is. That makes the cause and effect obvious, because you touch the lid and get slapped right there. We put the electronics on top of a box next to the jar. The USB speaker gives the jar a voice, so it feels like a character scolding you instead of a machine. It tells you that it is a normal cookie jar until you touch the lid and the moment you do it scolds you.
- What thresholds, timing, or movement patterns make the interaction feel clear or playful?
1. Escalation: the jar gets angrier each time, so people understand they’re being warned and keep trying to see what happens next. That’s the playful part.
2. Slap motion: the arm swings out fast and pauses for 0.25 seconds so the hit lands, then comes back slowly. That makes it look like a deliberate slap, not a twitch.
3. Speaking while slapping: the jar talks at the same time the arm moves, so the line and the slap feel like one reaction.
4. Cooldown: a 1-second pause after each reaction keeps one long grab from counting as several touches.
5. Calm-down: after 10 seconds with no touches, the jar resets and says “Just a normal cookie jar.” That makes it feel like it’s pretending to be innocent again.
- What changes when you adjust the sensor placement or servo motion?
What changes is that the smaller the hand the easier it stays upright rather than being floppy. Also the speed is fast but not fast enough to hurt. It's fast enough to react and immediately hit someone if they touch the jar but not fast enough to hurt them.

---

### Part F
Looks Like:

The Lid Slapper is meant to look like an ordinary cookie jar sitting on a counter. The servo, the Pi and the wiring are behind it in a cardboard base that is next to the jar, so nothing gives away that it’s watching you. The copper tape on the lid is decorated as part of the lid. The cardboard slap arm sits next to the jar on the cardboard box that is hiding all the stuff at rest, so it doesn’t stand out until it swings. The USB speaker is hidden inside the base with all the wiring, so the voice seems to come from the jar itself.

Works Like:

- Sensing: copper tape on the lid is wired to the MPR121 capacitive touch sensor, which detects the moment a hand touches the lid.
- Actuation: a micro servo on the Servo pHAT swings a cardboard arm to slap the hand away.
- Voice: the jar speaks through a USB speaker using the Piper voice from Lab 3.
- Escalation:
	- 1st touch: wiggles and says “I see you. Put it down.”
	- 2nd touch: slaps and says “I said no! Slap!”
	- 3rd touch and after: double slaps and says “Cookie police! Slap slap!”
- Reset: after 10 seconds with no touches, it calms down and says “Just a normal cookie jar.”
- Code: lid_slapper.py

Acts like:

Someone walks up to what looks like a normal cookie jar and reaches for the lid. As soon as they touch it, the jar warns them. Most people laugh and try again, and the second try earns a slap. Anyone who keeps going gets the double slap and “Cookie police!” If they give up and walk away, the jar goes quiet and pretends to be innocent until the next person comes along.

### Final Documentation



---
