#!/usr/bin/python3
# import necessary libraries
from gpiozero import Button, RGBLED
import random, time

# define objects for gpiozero
btnR = Button(19)
btnB = Button(26)
RGB = RGBLED(22,27,17)

# set variables for easily referring to colors
red = (1,0,0)
green = (0,1,0)
blue = (0,0,1)

# define a function to monitor for button presses
def monitorButtons(seconds):
    # loop for specified time, checking for button press
    timeEnd = time.time() + seconds
    while time.time() < timeEnd:
        if btnR.is_pressed:
            return announceWinner(btnR)
        if btnB.is_pressed:
            return announceWinner(btnB)
    return False

# define a function to announce the winner
def announceWinner(btn):
    # determine if LED was green when button was pressed
    if RGB.color == green:
        # button press was valid, player wins!
        winner = red if btn == btnR else blue
    else:
        # button press was invalid, opponent wins!
         winner = blue if btn == btnR else red
    # flash winning color 5 times
    RGB.blink (on_color = winner, n = 5, background = 0)

# play the game, loop until a button is pressed
btnPressed = False
while btnPressed == False:
    # select a random color
    ledColor = random.choice([red,green,blue])
    # play through one color cycle
    RGB.color = ledColor             # turn on LED
    btnPressed = monitorButtons(.5)   # monitor buttons


