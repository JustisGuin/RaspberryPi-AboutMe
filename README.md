# Reaction Game 
  Now we're going to make a 2 player quick-reaction game, designed to see who has the quickest reflexes!
---
---
## Setting up the Pi

  For this game you'll need a breadboard, an LED, a 200Ω resistor, two push buttons, some male-to-female jumper wires, and some male-to-male jumper wires.<br>
  Start by building the circut: connect the first button at the left hand side of your breadboard to the GPIO 14 pin, the second button at the right-hand side of your breadboard to the GPIO 15 pin, the LED's longer leg to the 200Ω resistor which then connects to the GPIO 4 pin of Rasperry Pi, and the second legs on all your components to your breadboard's ground rail. Finally, connect the ground rail to Rasperry Pi's ground pin.
## Writing the code

  Now you're going to be using the LED Button functions from the GPIO Zero library, and the time library. Rather than importing the two GPIO Zero functions on two seperate lines, you can save time and space by using a comma symbol (,) to seperate them. This is what your code should look like:<br>
 <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/WritingTheCode01.jpg"><br><i>Figure 3.1: Imports you need.</i></kbd><br>

  As before you'll need to tell GPIO Zero which pins the two buttons and LED are connected to. Type the Following:<br>
  <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/WritingTheCode02.jpg"><br><i>Figure 3.2: Variables you'll need to define.</i></kbd><br>
  >The number thats in the () depends on the GP# pin you connected the Buttons/LED to on your Raspberry Pi<br>

  Now add instructions to turn the LED on and off, so you check it's working correctly:<br>
  <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/WritingTheCode03.jpg"><br><i>Figure 3.3: Light pattern.</i></kbd><br>

  Run the program: the LED will turn on for five seconds, then turn off and the program will quit. For the purposes of a reaction game, though, having the LED go off after exactly five seconds every time is a bit predictable. So add the following below the line `import time`:<br>
  <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/WritingTheCode04.jpg"><br><i>Figure 3.4: Function to randomize the time.</i></kbd><br>
 
  The random library, as it's name suggests, lets you generate random numbers. Find the line `sleep(5)` and change it to:<br>
  <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/WritingTheCode05.jpg"><br><i>Figure 3.5: Randomizing the time.</i></kbd><br>

  Run the program again: this time the LED will stay lit for a random number of seconds between 5 and 10. Count to see how long it takes for the LED to go off, then run it a few more times. You'll see the outcome is different each time, making guessing when the button goes off virtualy impossible.<br>
  To make the buttons triggers for both players, you'll need to create a new function. Go to the very bottom of your code and type the following:<br>
  <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/WritingTheCode06.jpg"><br><i>Figure 3.6: pressed Function.</i></kbd><br>

  Remember that Python uses indentation to know which lines are part of your function; Thonny will automatically ident the next line for you. Finally, add the following two lines to detect which players are pressing the buttons - remembering that they must not be indented or they will be considered part of your function: pressed().<br>
  <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/WritingTheCode07.jpg"><br><i>Figure 3.7: Right or Left pressed.</i></kbd><br>

  Run your program, and this time try to press one of the two buttons as soon as the LED goes out. You'll see a message for the first button to be pushed printed to the Python shell at the bottom of the Thonny window. Unfortunately, you'll also see messages for each time either button is pushed - and they use the pin number rather than a friendly name for the button.<br>
  To fix that, start by asking the players for thier names. Underneath the line `from random import uniform`, type the following:<br>
  <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/WritingTheCode08.jpg"><br><i>Figure 3.8: Inputing Names.</i></kbd><br>
  
  Go back to your function and replace the line `print(str(button.pin.number) + " won the game!")` with:<br>
    <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/WritingTheCode09.jpg"><br><i>Figure 3.9: If Else statement.</i></kbd><br>

  Now run the program, and type your names into the PowerShell area. When you run the program this time, remembering to push your button as fast as you can once the LED goes out. This time you'll notice that the winning player's name is shown instead of the pin number.<br>
  To fix the problem of all button presses being reported as having won, you'll need to add a new function from the system library: <b>exit</b> Under the last <b>import</b> line, type the following:
  INSERT PICTURE<br>
  from os import _exit<br>
  <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/WritingTheCode10.jpg"><br><i>Figure 3.10: Importing _exit.</i></kbd><br>
  
Then at the end of your function, under the line `print(rightName + " won the game!")`, type the Following:<br>
  INSERT PICTURE<br>
  _exit(0)<br>
  <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/WritingTheCode11.jpg"><br><i>Figure 3.11: exit method.</i></kbd><br>

  The indentation is important here: `_exit(0)` should be indented lining up with `else:`. This instruction tells Python to stop the program after the first button is pressed, meaning the person who pressed their button second doesn't get any reward for losing!<br>
  Your finished program should look like this:

## Challenges
### Challenge 1:
Make the Program welcome the user before the asking the names. Have it say this:<br>
<kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/Challenges01.jpg"><br><i>Figure 4.1: Welcome text.</i></kbd><br>

### Challenge 2: 
Make the terminal reset once the winner has been decided so it can be ready for new players.

### Challenge 3:
Make it a best out of 3 competition between the two players

### Challenge 4:
Find how much time elapsed from the first button being pushed to the second one. Have the Terminal output something like this:<br>
<kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/Challenges04.jpg"><br><i>Figure 4.2: Millisecond text.</i></kbd><br>

### Challenge 5:
Find the Average of the winners millisecond times to get an accurate winning time
