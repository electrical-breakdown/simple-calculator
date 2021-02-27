# Simple Calculator

A simple calculator project to help me learn the basics of using tkinter.



## Summary

This was my first time using tkinter to make a GUI. I started watching the freecodecamp.com class on YouTube, and followed along with their calculator project. After using their basic layout, I went off on my own to pogram the logic. I wasn't happy at all with the default design, so I wanted to try my hand at creating something a little nicer looking. 



## Design

The color scheme was loosely based on the iOS calculator and I laid out the design in Figma. When it came time to build the layout in tkinter, I quickly learned that sizing components in pixels was harder than it seemed. After some Googling, I found that I could wrap the buttons in frames and then use pixel dimensions to size the frames. The grid() method of placement didn't seem to offer the precision I was looking for, so I opted to use place() so I could place everything everything exactly where I wanted it. 


<img src="/calculator_mockup.png" alt="image of the calculator design made in Figma" height="244px" width="164px" />



## Code

When I thought about how I wanted to go about the logic, my approach was to use a list to keep a running tally of all the numbers and operations entered into the calculator, and then evaluate everything in the list when the equals button is pressed. I used the eval() function for this, which I understand may be undesirable in some instances. In hindsight, I realized I didn't really need to keep a running tally of everything, and really only needed two values - the current value, and the previous value. With those two values, I could continutally add, subtract, multiply, etc. in a linear sequence.

I used nested loops to generate the frames and buttons because I thought that creating all of them manually seemed tedious. The loops weren't as easy as they first seemed, because some of the buttons needed different functions. I ended up using lambdas to pass the value of the button into a single button_click() function. Then used a kind of ugly if/else to determine how to handle each button click based on the value passed in from the button. 



## What's next

In the next iteration, I'd like to add some validation to the entry widget to restrict keyboard input to just the characters found on the GUI. I may also rewrite the logic as the way I did it feels a little gross, and I'm sure I can find a cleaner way next time. Looking forward to making GUIs for some of the other little Python games I've made. 


