#Modules

from operator import truediv
import time
import random
import os
import colorama
import sys

#Variables

running = True
active = True
inventory = []
typetime = 0.06
WaitTimeBetweenSentence = 0.3
PlayerColor = colorama.Fore.CYAN
CharacterColor = colorama.Fore.RED
ChoiceMenuColor = colorama.Fore.GREEN
TextColor = colorama.Fore.WHITE
Speaker = ""

#Functions

def end():
    active = False
    quit()

def wait(GivenTime):
    time.sleep(GivenTime)

def speak(s,v):
    global WaitTimeBetweenSentence
    global Speaker
    global typetime
    global CharacterColor

    sys.stdout.write(CharacterColor +Speaker + ": ")

    wait(WaitTimeBetweenSentence)

    for c in s:
        sys.stdout.write(TextColor + c)
        sys.stdout.flush()
        time.sleep(typetime)

    if v == 1:
        print('')

while(active == True):
    os.system("cls")
    Speaker = "???"

    speak("Hey!",1)
    speak("You there!",1)
    speak("Wake up!",1)
    end()
