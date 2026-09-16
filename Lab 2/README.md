# Interactive Prototyping: The Clock of Pi
**NAMES OF COLLABORATORS HERE**
- Gaurav Patel gp438
- Nishant Ray nr487
- Neeha Ravula nr485
- Victor Radev vr373


Does it feel like time is moving strangely during this semester?

For our first Pi project, we will pay homage to the [timekeeping devices of old](https://en.wikipedia.org/wiki/History_of_timekeeping_devices) by making simple clocks.

It is worth spending a little time thinking about how you mark time, and what would be useful in a clock of your own design.

**Please indicate anyone you collaborated with on this Lab here.**
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

## Prep

1. ### Set up your Lab 2 Github

At the start of lab Wednesday, ensure you have the latest lab content by updating your forked repository. 

**📖 [Follow the step-by-step guide for safely updating your fork](pull_updates/README.md)**

This guide covers how to pull updates without overwriting your completed work, handle merge conflicts, and recover if something goes wrong.


2. ### Get Kit and Inventory Parts
Take inventory of the kit parts that you have, and note anything that is missing:

***Update your [parts list inventory](partslist.md)***

3. ### Prepare your Pi for lab this week
[Follow these instructions](prep.md) to download and burn the image for your Raspberry Pi before lab Wednesday.




## Overview
For this assignment, you are going to 

A) [Connect to your Pi](#part-a)  

B) [Try out cli_clock.py](#part-b) 

C) [Set up your RGB display](#part-c)

D) [Try out clock_display_demo](#part-d) 

E) [Modify the code to make the display your own](#part-e)

F) [Make a short video of your modified barebones PiClock](#part-f)

G) [Sketch and brainstorm further interactions and features you would like for your clock for Part 2.](#part-g)

## The Report
This readme.md page in your own repository should be edited to include the work you have done. You can delete everything but the headers and the sections between the \*\*\***stars**\*\*\*. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in the readme.

Labs are due on Sunday midnight. Make sure this page is linked to on your main class hub page.

## Part A. 
### Connect to your Pi
Just like you did in the lab prep, ssh on to your pi. Once you get there, create a Python environment (named venv) by typing the following commands.

```
ssh pi@<your Pi's IP address>
...
pi@raspberrypi:~ $ python -m venv venv
pi@raspberrypi:~ $ source venv/bin/activate
(venv) pi@raspberrypi:~ $ 

```
### Setup Personal Access Tokens on GitHub
Set your git name and email so that commits appear under your name.
```
git config --global user.name "Your Name"
git config --global user.email "yourNetID@cornell.edu"
```

**The Personal Access Token on Git and the Python Environment have been created**

## Part B. 
### Try out the Command Line Clock

<img width="1086" height="68" alt="image" src="https://github.com/user-attachments/assets/99b44710-d9fb-4142-bdd1-9dd28bfcee25" />

## Part C. 
### Set up your RGB Display

**Raspberry Pi Displaying the piscreen with Mac Address**
<img width="3024" height="4032" alt="IMG_2096" src="https://github.com/user-attachments/assets/52001955-4b43-494c-8028-420ebc2c9936" />

**Raspberry Pi with Chosen Color Green**
<img width="3024" height="4032" alt="IMG_2095" src="https://github.com/user-attachments/assets/adbf52d5-b090-4542-9720-13a859be8370" />



## Part D. 
### Set up the Display Clock Demo

<img width="3024" height="4032" alt="IMG_2097" src="https://github.com/user-attachments/assets/f5244c65-4bc9-46ef-9626-0fe7fcafcc51" />


## Part E. Read Part 2. Sketch and brainstorm further interactions and features you would like for your clock.

## Concept: Spider-Verse Clock

Instead of showing literal time, a chibi Spider-Man mascot swaps suits every hour (24 suits total, one per hour). Each suit has a signature food, and the number of food items shown scales with the hour.

| Hour | Suit | Food (qty = hour) |
|---|---|---|
| 8am | Spider-Man India (Pavitr) | 8 cups of chai |
| 12pm | Spider-Ham (Peter Porker) | 12 mini pies |
| 3pm | Miles Morales | 3 pizza slices |
| 6pm | Peter Parker (classic) | 6 of Aunt May's pies |
| 12am | Spider-Gwen | 12 donuts |
| 2am | Spider-Man Noir | 2 cups of coffee |

**Interaction loop:** clock ticks → pick suit for current hour → render mascot + food count → repeat every hour.

**Extension ideas:**
- Button press = "spider-sense" easter egg, flashes a random alt suit
- Midnight = full-screen suit montage
- 
<img width="2244" height="2904" alt="Piclock Spiderman-1" src="https://github.com/user-attachments/assets/7ad4ed6a-b4cb-4be0-a0f9-5f99353d6418" />




**Put the names of the people you gave feedback to here. (Even better, add links to their repos here!)**
**Jovian Wang(https://github.com/jovianw/Interactive-Lab-Hub):** Hello Jovian, your design is very straightforward and uses the natural time of a plant growing and the movement of the sun to denote time passing! Something missing from the sketch is what happens to the plant when night time occurs? From the storyboard it just looks like the plant disappears and there is no moon or anything to indicate that it's night time. Perhaps adding the moon and stars would be a important feature to add to help show the user what time it is at night. Perhaps the number of petals says how many minutes have passed. There is a lot of things you can do. Overall very good design!

**Ammar Syed(https://github.com/ammarsyed/Interactive-Lab-Hub/blob/Fall2026/Lab%202/README.md):** I like the idea of using an hourglass as a way to represent time. It’s something that everyone is familiar with so it’s very intuitive and gives a clear visual sense of time passing. Though I would say I always personally found hourglasses to be a little ambiguous in regard to how much time is left for it to finish ticking. I’d be interested in seeing how you could make the concept feel a little more unique or personal beyond a traditional hourglass.

**Pallavi Khanna(https://github.com/pk633-cu/Interactive-Lab-Hub/blob/Fall2026/Lab%202/README.md):** Feedback - Overall, I like the first idea, it seems like it is easy to tell time because the sunset is very recognizable. I like the idea that the sun's height will represent time. I am curious about the minutes thought will the sun only change per hour or will it slowly rise per minute. I think that is something that is probably an important distinction to make. The second idea is a little confusing. I don't understand fully what the buildings are representing? Like do they have any indication on the time or is it just the weather/sun? I like the last idea too where there is a step's associated with the clock. It tells you what time you need to have the steps done by. However it doesn't seem like a clock more like a goal that is needed to be achieved in that time-frame.

**Rohil Saraf(https://github.com/rohilsaraf97/Interactive-Lab-Hub/blob/Fall2026/Lab%202/README.md#part-e-read-part-2-sketch-and-brainstorm-further-interactions-and-features-you-would-like-for-your-clock):** Great design! Simple and does the job, just wondering if using 8 cups of chai or 2 cups of coffee counts as numerical representation? Also, if it doesn't, then something like using the chai and coffee cups etc. could be useful to represent another dimension, like minutes, and maybe the Spiderman variant, the background, and the animation could represent the hour? I was just thinking that since you have 24 Spiderman variations, representing the hours with a different prop might be redundant. Is finding Spidermen that look considerably different on such a small screen easy? maybe even a spiderman going to bed could mean its night time, time to go to bed, like does it have to convey actual time? It could revolve around your activities for the day maybe? Also, super cute diagrams!!

# Lab 2 Part 2

## Prep 

1. Pick up remaining parts for kit on Wednesday lab class. Check the updated [parts list inventory](partslist.md) and let the TA know if there is any part missing.

2. Look at and give feedback on the Part E. for at least 3 other people in the class and get 3 people to comment on your Part E!)
**Put the feedback for your ideas here.**

**Ammar Syed: ** The Spider Verse clock is a super creative way to represent time, far different than a traditional digital or analog display. I really like how each hour has a different Spider Man suit and a correlated food related to that suit. The quantity of that food is what correlates to the actual time. It is very playful and visually unique.

My only concern is that displaying that many items at a high numbered time like 12:00, which means 12 food items, might make this small screen very crowded. Maybe you can adjust that by using one food icon and then a number, either inside or to the side of that food item, to show the relevant time.

**Pallavi Khanna: ** Feedback - Overall, I like the first idea, it seems like it is easy to tell time because the sunset is very recognizable. I like the idea that the sun's height will represent time. I am curious about the minutes thought will the sun only change per hour or will it slowly rise per minute. I think that is something that is probably an important distinction to make. The second idea is a little confusing. I don't understand fully what the buildings are representing? Like do they have any indication on the time or is it just the weather/sun? I like the last idea too where there is a step's associated with the clock. It tells you what time you need to have the steps done by. However it doesn't seem like a clock more like a goal that is needed to be achieved in that time-frame.

**Jovian Wang: ** I love the design! The spider man theme is a very fun take and shows a lot of creativity. While I like the idea of the number of foods showing the time, I am a little concerned about the readability of the clock! If they were somewhat randomly placed liked the current storyboard, I fear the user might have a difficult time interpreting the hour number. I think a good compromise could be the foods moving around in a predictable circle around the spiderman -- it's much more easier to tell when there are two, four, or eight objects around in a circle rather than randomly placed. You could probably find another compromise as well. Good job!

**Rohil Saraf: ** Snacks are the best! Your snack clock is very fun and very thought out and I can see the tie in between an animated characters body language to denote how much time has passed since the user last ate a snack. I think some fun metrics to add to the clock would be how many snacks you did eat throughout the day and perhaps changing how the character (physically, fatter, skinner, based on the amount of snacks it had during the week). Overall very good design, and you can go very far with it. The only feedback I have is perhaps adding interaction based on the amount of snacks eaten would also be interesting to implement.

## Update your Lab Hub

[Update your Lab Hub](pull_updates/README.md) to get the latest content and requirements for Part 2.

## Modify the barebones clock to make it your own

Start small, pick just one element of your overall idea, just to show you have a handle on the code and components.

\*\*\***Put a copy of your code in your Lab 2 Github repo.**\*\*\*

## Make a short video of your modified barebones PiClock

\*\*\***Take a video of your barely modified PiClock.**\*\*\*

After you edit and work on the scripts for Lab 2, the files should be upload back to your own GitHub repo! You can push to your personal github repo by adding the files here, commiting and pushing.

```
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git add .
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git commit -m 'your commit message here'
(venv) pi@raspberrypi:~/Interactive-Lab-Hub/Lab 2 $ git push
```

After that, Git will ask you to login to your GitHub account to push the updates online, you will be asked to provide your GitHub user name and password. Remember to use the "Personal Access Tokens" you set up in Part A as the password instead of your account one! Go on your GitHub repo with your laptop, you should be able to see the updated files from your Pi!

## Now, make your own PiClock

Do take advantage of having done the previous iteration to refine and simplify your design.

** Insert any updates ideas, sketches, [Verplank diagrams](https://ccrma.stanford.edu/courses/250a-fall-2004/IDSketchbok.pdf))!, storyboards for your ideas **


\*\*\***Put a copy of your code in your Lab 2 Github repo.**\*\*\*

\*\*\***Take a video of your PiClock.**\*\*\*


As always, make sure you document contributions and ideas from others (and AI) explicitly in your writeup.

You are permitted (but not required) to work in groups and share a turn in; you are expected to make equal contribution on any group work you do, and N people's group project should look like N times the work of a single person's lab.  Make sure the page for the group turn in is linked to your personal Interactive Lab Hub page. 


