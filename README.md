# Raspberry Pi
---
---
## How to use RaspberryPi 

## Traffic Lights 


## Reaction Game 

#### Setting up the Pi

#### Writing the code
  Now you're going to be using the LED Button functions from the GPIO Zero library, and the time library. Rather than importing the two GPIO Zero functions on two seperate lines, you can save time and space by using a comma symbol (,) to seperate them. This is what your code should look like:
INSERT PICTURE
  from gpiozero import LED, Button
  import time

  As before you'll need to tell GPIO Zero which pins the two buttons and LED are connected to. Type the Following:
INSERT PICTURE
  led = LED(4)
  rightBTN = Button(15)
  leftBTN = Button(14)
  (small text under picture) It depends on the GP# you are using

  Now add instructions to turn the LED on and off, so you check it's working correctly:
  INSERT PICTURE
  led.on()
  sleep(5)
  led.off()

  Run the program: the LED will turn on for five seconds, then turn off and the program will quit. For the purposes of a reaction game, though, having the LED go off after exactly five seconds every time is a bit predictable. So add the following below the line __import time__:
  INSERT PICTURE
  from random import uniform
 
  The random library, as it's name suggests, lets you generate random numbers. Find the line __sleep(5)__ and change it to:
  INSERT PICTURE
  sleep(uniform(5,10))

  Run the program again: this time the LED will stay lit for a random number of seconds between 5 and 10. Count to see how long it takes for the LED to go off, then run it a few more times. You'll see the outcome is different each time, making guessing when the button goes off virtualy impossible.
  To make the buttons triggers for both players, you'll need to create a new function. Go to the very bottom of your code and type the following:
  INSERT PICTURE
  def pressed(button):
    print(str(button.pin.number) + " won the game!")

  Remember that Python uses indentation to know which lines are part of your function; Thonny will automatically ident the next line for you. Finally, add the following two lines to detect which players are pressing the buttons - remembering that they must not be indented or they will be considered part of your function: pressed().
  INSERT PICTURE
  rightBTN.when_pressed = pressed
  leftBTN.when_pressed = pressed

  Run your program, and this time try to press one of the two buttons as soon as the LED goes out. You'll see a message for the first button to be pushed printed to the Python shell at the bottom of the Thonny window. Unfortunately, you'll also see messages for each time either button is pushed - and they use the pin number rather than a friendly name for the button.
  To fix that, start by asking the players for thier names. Underneath the line __from random import uniform__, type the following:
  INSERT PICTURE
  leftName = input("Left player, Type Name: ")
  rightName = input("Right player, Type Name: ")
  
  Go back to your function and replace the line __print(str(button.pin.number) + " won the game!")__ with:
  INSERT PICTURE
  if button.pin.number == 14:
    print(leftName + " won the game!")
  else:
    print(rightName + " won the game!")

  Now run the program, and type your names

#### Playing the game

#### Challenges
