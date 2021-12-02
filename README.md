# Raspberry Pi
---
---
## How to use RaspberryPi 

## Traffic Lights 


## Reaction Game 

### Setting up the Pi

### Writing the code
  Now you're going to be using the LED Button functions from the GPIO Zero library, and the time library. Rather than importing the two GPIO Zero functions on two seperate lines, you can save time and space by using a comma symbol (,) to seperate them. This is what your code should look like:<br>
INSERT PICTURE<br>
  from gpiozero import LED, Button<br>
  import time<br>
 <kbd><img src=""><br><i>Figure 3.1: Imports you need.</i></kbd><br>

  As before you'll need to tell GPIO Zero which pins the two buttons and LED are connected to. Type the Following:<br>
INSERT PICTURE<br>
  led = LED(4)<br>
  rightBTN = Button(15)<br>
  leftBTN = Button(14)<br>
  <kbd><img src=""><br><i>Figure 3.2: Variables you'll need to define.</i></kbd><br>
  ><font size="1">It depends on the GP# you are connecting the Buttons/LED with on your Raspberry Pi</font><br>

  Now add instructions to turn the LED on and off, so you check it's working correctly:<br>
  INSERT PICTURE<br>
  led.on()<br>
  sleep(5)<br>
  led.off()<br>

  Run the program: the LED will turn on for five seconds, then turn off and the program will quit. For the purposes of a reaction game, though, having the LED go off after exactly five seconds every time is a bit predictable. So add the following below the line `import time`:<br>
  INSERT PICTURE<br>
  from random import uniform<br>
 
  The random library, as it's name suggests, lets you generate random numbers. Find the line `sleep(5)` and change it to:<br>
  INSERT PICTURE<br>
  sleep(uniform(5,10))<br>

  Run the program again: this time the LED will stay lit for a random number of seconds between 5 and 10. Count to see how long it takes for the LED to go off, then run it a few more times. You'll see the outcome is different each time, making guessing when the button goes off virtualy impossible.<br>
  To make the buttons triggers for both players, you'll need to create a new function. Go to the very bottom of your code and type the following:<br>
  INSERT PICTURE<br>
  def pressed(button):<br>
    print(str(button.pin.number) + " won the game!")<br>

  Remember that Python uses indentation to know which lines are part of your function; Thonny will automatically ident the next line for you. Finally, add the following two lines to detect which players are pressing the buttons - remembering that they must not be indented or they will be considered part of your function: pressed().<br>
  INSERT PICTURE<br>
  rightBTN.when_pressed = pressed<br>
  leftBTN.when_pressed = pressed<br>

  Run your program, and this time try to press one of the two buttons as soon as the LED goes out. You'll see a message for the first button to be pushed printed to the Python shell at the bottom of the Thonny window. Unfortunately, you'll also see messages for each time either button is pushed - and they use the pin number rather than a friendly name for the button.<br>
  To fix that, start by asking the players for thier names. Underneath the line `from random import uniform`, type the following:<br>
  INSERT PICTURE<br>
  leftName = input("Left player, Type Name: ")<br>
  rightName = input("Right player, Type Name: ")<br>
  
  Go back to your function and replace the line `print(str(button.pin.number) + " won the game!")` with:<br>
  INSERT PICTURE<br>
  if button.pin.number == 14:<br>
    print(leftName + " won the game!")<br>
  else:<br>
    print(rightName + " won the game!")<br>

  Now run the program, and type your names into the PowerShell area. When you run the program this time, remembering to push your button as fast as you can once the LED goes out. This time you'll notice that the winning player's name is shown instead of the pin number.<br>
  To fix the problem of all button presses being reported as having won, you'll need to add a new function from the system library: <b>exit</b> Under the last <b>import</b> line, type the following:
  INSERT PICTURE<br>
  from os import _exit<br>
  
Then at the end of your function, under the line `print(rightName + " won the game!")`, type the Following:<br>
  INSERT PICTURE<br>
  _exit(0)<br>

  The indentation is important here: `_exit(0)` should be indented lining up with `else:`. This instruction tells Python to stop the program after the first button is pressed, meaning the person who pressed their button second doesn't get any reward for losing!<br>
  Your finished program should look like this:

#### Playing the game

#### Challenges
