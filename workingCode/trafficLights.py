from gpiozero import Button
from time import sleep
from gpiozero import LED
from gpiozero import Buzzer

buzzer = Buzzer(15)
button = Button(2)
led25= LED(25)
led8= LED(8)
led7= LED(7)

#button.wait_for_press()
#Uk Traffic lights without Button
"""
sleep(5)
led8.on()
sleep(2)
led25.off()
led8.off()
led7.on()

sleep(5)
led7.off()
led8.on()
sleep(5)
led8.off()
"""
#pedestrain Crossing with button


#button.when_for_press()
#if pressed#

i = 0
def pressed():
    led25.on()
    while i<10:
        buzzer.on()
        sleep(.2)
        buzzer.off()
        sleep(.2)

led25.on()
sleep(5)
led25.off()
led8.on()
sleep(2)
led8.off()
#led8.off()
led7.on()
sleep(5)
led7.off()
led8.on()
sleep(5)
led8.off()


    
button.when_pressed=pressed
#while True:

