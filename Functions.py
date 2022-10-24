#Modules

from operator import truediv
import time
import random
import os
import colorama
import sys

#Functions

def end():
    active = False
    quit()

def clearscreen():
    os.system("cls")

def wait(GivenTime):
    time.sleep(GivenTime)

def changespeaker(sp):
    global Speaker
    Speaker = sp

def speak(s,v):
    from Hello_YouStory import changespeaker
    global WaitTimeBetweenSentence
    global Speaker
    global typetime
    from Variables import CharacterColor
    from Variables import WaitTimeBetweenSentence
    from Variables import typetime

    sys.stdout.write(CharacterColor +Speaker + ": ")

    wait(WaitTimeBetweenSentence)

    for c in s:
        sys.stdout.write(TextColor + c)
        sys.stdout.flush()
        time.sleep(typetime)

    if v == 1:
        print('')
