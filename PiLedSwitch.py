#Python3 Script Unsing GPIO Zero Library for Raspberry Pi - Leo Massarani

print("\nGPIO Program LM 07-Jul-18 v0.1  -  Need ROOT Priviledges\n")

#Make sure we are running on Raspberry Pi
import os
if (os.system("cat /etc/os-release | grep Raspbian -m 1") == 0):
#    print("Running on Raspberry: %s", os.system("cat /etc/os-release | grep Raspbian -m 1"))
     print("Looks like we are running on Raspberry\n")
else:
    print("Program can only run on Raspberry Pi\n") 
    exit()

#Import the Libraries
from gpiozero import LED, Button
from time import sleep
import sys
print ("LED and sleep libraries imported\n")

#GPIO Pin 17 will have an LED then resistor to ground
led17 = LED(17)

#Initial Blink Sequence
print ("LED on GPIO 17 will blink 3 times:",end=" ")
times = 3
while (times > 0):
    led17.on()
    print(".",end=" ")
    sys.stdout.flush()
    sleep(1)
    led17.off()
    sleep(1)
    times = times - 1

#Check for button press - GPIO 5 will have a button input with button connected to ground when pressed
button5 = Button(5)

#Control LED on Button Press
print("\n\nLED on GPIO 17 will be ON while button in GPIO 5 is pressed (_), off when button is released(T):\n")
while True:
    if button5.is_pressed:
        led17.on()
        print("_",end="")
    else:
        led17.off()
        print("T",end="")
    sys.stdout.flush()
    sleep(0.1)

