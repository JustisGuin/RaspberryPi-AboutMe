from gpiozero import LED, Button
import time
from random import uniform
from os import _exit

leftName = input("Left player, Type Name: ")
rightName = input("Right player, Type Name: ")
led = LED(4)
rightBTN = Button(15)
leftBTN = Button(14)

led.on()
time.sleep(uniform(5,10))
led.off()

def pressed(button):
    if button.pin.number == 14:
        print(leftName + " won the game!")
    else:
        print(rightName + " won the game!")
    _exit(0)

rightBTN.when_pressed = pressed
leftBTN.when_pressed = pressed

