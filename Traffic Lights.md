# Traffic Lights  Setup Tutorial

## Step 1 Connect Button To Bread Board 

<img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/20211130_130514.jpg" height="400px" width="500px"></kbd>

   -You need to take the button and line it up where the legs are going into 2 and 4 right under e 
   
   -Put other side of the legs under the g
   
### Second Step 
  <img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/20211130_130549.jpg" height="400px" width="500px"></kbd>
  
  
   -Now you Want to Grab a male to male wire 
   
   -Plug it in the right side negative on 5 and the other side right beside the right side of the button on 2 under 
   
### Third Step 
   <img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/20211130_130916.jpg" height="400px" width="500px"></kbd>
   
   -You are going to connect the white wire (or what ever color it is) to d,4 
   
   -Connect the female side to the Pi then connect it to the GP2 connection
   
   
# Connecting the Lights to the Bread Board 

   ## Red Light
   
   ### First Step
         
   <img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/Image%20from%20iOS.jpg" height="400px" width="500px"></kbd>
   
   
   -On the right side on the Bread Board connect the red light short side on the - between 15 and 16 
   
   -Connect the Long side of the red light on J,15
   
   ### Second Step
   -Connect the resistor (either way) on H,15 and then the other side on the left side of the board on E,15
   
   -Your going to take a female to male wire and connect it right next to the resistor D,15
   
   -Connect the female side of the wire to the GP25 connection on the Pi 
   
   
   ## Yellow Light
   
   ### First Step 
   
   <img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/Image%20from%20iOS%20(1).jpg" height="400px" width="500px"></kbd>
   
   -Connect the short side on the yellow light to the - inbetween 21 and 22
   
   -Connect the long side to J,21
   
   ### Second Step 
   
   -Connect the resistor (either way) on H,21 then on the left side of the board on E,21 
   
   -Your going to take a female to male wire and connect it right next to the resistor D,21
   
   -Connect the female side of the wire to the GP8 connection on the Pi 
   
   ## Green Lights
   
 
   ### First Steps 
   <img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/Image%20from%20iOS%20(2).jpg"  height="400px" width="500px"></kbd>
   
   -Connect the short side on the green light to the - inbetween 27 and 28 
   
   -Connect the long side to J,27
   
   ### Second Step
   
   -Connect the resistor (either way) on H,27 then on the left side of the board on E,27
   
   -Your going to take a female to male wire and connect it right next to the resistor D,27
   
   -Connect the female side of the wire to the GP7 connection on the Pi 
   
   
   
   ## Finished Product 
   <img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/20211118_131232.jpg" height="400px" width="500px"></kbd>
   
   
   
   
   # Writing the code 
   Now you're going to be using Button from the gpio library, the time library. Your not going to use the buzzer in this Traffic Light Project so you can leave that out. This is what    your code should look like:<br>
   <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/Traffic%20Lights%20Imports.png"><br><i>Figure 3.1: Imports you need.</i></kbd><br>
   
   
   
  Now add instructions to turn the LED on and off, so you check it's working correctly:<br>
  <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/Assigning%20the%20buzzer%20and%20such.png"><br><i>Figure 3.3: Light pattern.</i></kbd><br>
      
   To allow the button to have any purpose. Your going to need to add code for the button to know what to do. You are going add a function named pressed() after you assigned the buzzer,button,led25,led8 and led7. The following should look like this:
   <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/pressed()%20function.png"><br><i>Figure 3.2: pressed Function.</i></kbd><br>
   
   
   
   When you run your program and press the button it does nothing. The reason this is because your not telling the lights to do anything when the button is pressed. Your going to add the following to allow your red,yellow and green light to turn on:
   <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/leds%20on%20and%20off.png"><br><i>Figure 3.3: led on and off.</i></kbd><br>
   

   Your going to run your program and see that nothing is happening still even after you assigned your led's to turn on and off. But your missing one important piece of code. The following code you want to enter is under the led8.off() type the following in:
    <kbd><img src="https://github.com/JustisGuin/RaspberryPi-AboutMe/blob/main/images/button.when_pressed.png"><br><i>Figure 3.4: Button.when_pressed /i></kbd><br>
   
   
   Congrats you have just made a traffic light simulation game. Test it out to see if you got everything correct! Don't have to much fun with it.
   

   
   
   
   
   
   
   
   
