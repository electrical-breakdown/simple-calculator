# Simple Calculator

A simple calculator project to help me learn the basics of using tkinter.

This was my first time using tkinter to make a GUI. I started watching the freecodecamp.com class on YouTube, and followed along with their calculator project. After using their basic layout, I went off on my own to pogram the logic. I wasn't happy at all with the default design, so I wanted to try my hand at creating something a little nicer looking. 

The color scheme was loosely based on the iOS calculator and I laid out the design in Figma. When it came time to build the layout in tkinter, I quickly learned that sizing components in pixels was harder than it seemed. After some Googling, I found that I could wrap the buttons in frames and then use pixel dimensions to size the frames. The grid() method of placement didn't seem to offer the precision I was looking for, so I opted to use place() so I could place everything everything exactly where I wanted it. 

<img src="/calculator_mockup.png" alt="image of the calculator design made in Figma" height="244px" width="164px" />


## What's new in Version 1.1

In the second iteration of this project, I added vaildation on the display widget to limit keyboard input to only specified keys. I also changed the way the buttons were created in version 1.0. Initially I thought it made sense to use loops to generate all the buttons, but that required me to use one large function for every button and use some unwieldy if/else statemnts to determine the proper action. 

In this version, I created the buttons individually which allowed me to specify a different function for each button as needed. I then used a loop to pack the buttons into their associated frames to cut down on the amount of repeated code. 

I also made some small tweaks to the behavior to mimic how the default iOS calculater works. 