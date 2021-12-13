# from gpiozero import LED, Button
# import time
# from random import uniform
# import os

# led = LED(4) # 4 is GP4 on the Raspberry
# rightBTN = Button(15) # GP15
# leftBTN = Button(14) #GP14
# # Never stops unless told to
# while True:
#     os.system("clear")
#     welcome = '''
#     Welcome to the Reaction Game!
#     Enter your names, and see who has the fastest reaction time!
#     After you enter your names, the light will iluminate. When the light
#     turns off, the race is on to see who can press their button the fastest!

#     '''
#     print(welcome)
#     leftName = input("Left player, Type Name: ")
#     rightName = input("Right player, Type Name: ")
#     results = ""

#     #turn the light on and off as a random time between 5 to 10 seconds
#     sleep(2)
#     led.on()
#     sleep(uniform(5,10))
#     led.off()
#     startTime = 0
#     endTime = 0

#     #Buttons have not been pressed
#     firstBTN = False
#     secondBTN = False

#     #if button was pressed
#     def pressed(button):
#         global startTime, secondBTN, firstBTN, endTime, results
#         if not firstBTN:
#             firstBTN = True
#             startTime = time.time()       
#             if button.pin.number == 14:
#                 results += rightName + " won the game!\n"
#             else:
#                 results += leftName + " won the game!\n"
#         elseif not secondBTN:
#             secondBTN = True
#             endTime = time.time()
#             results +=f"{round((endTime - startTime)*1000,2)} milliseconds between the buttons"
print('''

47.95 milliseconds between the buttons

''')
#     rightBTN.when_pressed = pressed
#     leftBTN.when_pressed = pressed
#     time.sleep(1)
#     print(results)
#     time.sleep(5)
#make best of 3


#average the winners times

