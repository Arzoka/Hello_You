#Modules

from operator import truediv
import time
import random
import os
import colorama
import sys
import pyaudio
import wave
import keyboard
from threading import Thread
from playsound import playsound

from Variables import ChoiceMenuColor, PlayerColor
from Variables import CharacterColor
from Variables import EventColor
from Variables import TextColor
from Variables import ActionColor
from Variables import ErrorColor

from Variables import typetime
from Variables import WaitTimeBetweenSentence

from Variables import actioncharacter

from Variables import Error1
from Variables import Error2

from Variables import Honesty
from Variables import Manipulation
from Variables import Comedy
from Variables import Bravery

from pynput.keyboard import Key, Listener

pressed = False

def on_press(key):
    global pressed
    if pressed == False:
        if result == 1:
            playsound('AudioFiles\\typesound.mp3', block=False)
        pressed = True

def on_release(key):
    global pressed
    pressed = False

# Collect events until released

result = 0

holding = False

def inputsound():
    while True:
        if result == 1:
            with Listener(
                on_press=on_press,
                on_release=on_release) as listener:
                listener.join()
        elif result == 0:
            break
    
#Functions

def DoError1():
    global ErrorColor
    global Error1

    print('')
    print(ErrorColor + Error1)
    print(TextColor + '')

def DoError2():
    global ErrorColor
    global Error2

    print('')
    print(ErrorColor + Error2)
    print(TextColor + '')

def end():
    active = False
    quit()

def ClearScreen():
    os.system("cls")

def wait(GivenTime):
    time.sleep(GivenTime)

def ChangeSpeaker(sp):
    global Speaker
    Speaker = sp

def ChangeSpeakerType(sptype):
    global SpeakType
    SpeakType = sptype

def ChoiceMenu2(s,s1):
    global ChoiceMenuColor
    global TextColor
    global ErrorColor
    global Error2

    ChoiceMenuRun = True
    while ChoiceMenuRun == True:
        print('')
        print(ChoiceMenuColor + "a)",s)
        print(ChoiceMenuColor + "b)",s1)
        print(TextColor + (''))
        answer = input().lower()
        if answer in["a","b"]:
            ChoiceMenuRun = False
            return answer
        else:
            DoError2()

def ChoiceMenu3(s,s1,s2):
    global ChoiceMenuColor
    global TextColor
    global ErrorColor
    global Error2
    global result

    ChoiceMenuRun = True
    while ChoiceMenuRun == True:
        print('')
        print(ChoiceMenuColor + "a)",s)
        print(ChoiceMenuColor + "b)",s1)
        print(ChoiceMenuColor + "c)",s2)
        print(TextColor)
        result = 1
        t = Thread(target=inputsound)
        t.start()
        answer = input().lower()
        result = 0
        if answer in["a","b","c"]:
            ChoiceMenuRun = False
            return answer
        else:
            DoError2()

def ChoiceMenu4(s,s1,s2,s3):
    global ChoiceMenuColor
    global TextColor
    global ErrorColor
    global Error2

    ChoiceMenuRun = True
    while ChoiceMenuRun == True:
        print('')
        print(ChoiceMenuColor + "a)",s)
        print(ChoiceMenuColor + "b)",s1)
        print(ChoiceMenuColor + "c)",s2)
        print(ChoiceMenuColor + "d)",s3)
        print(TextColor)
        answer = input().lower()
        if answer in["a","b","c","d"]:
            ChoiceMenuRun = False
            return answer
        else:
            DoError2()

def Event(s,v):
    global EventColor
    global TextColor
    global Honesty
    global Manipulation
    global Comedy
    global Bravery
    global Error1

    print('')

    s1 = "+"+str(v)+" "+s

    for c in s1:
        sys.stdout.write(EventColor + c)
        sys.stdout.flush()
        time.sleep(typetime)
    
    if s.lower() == "honesty":
        Honesty = Honesty + v
        sys.stdout.write(" ("+str(Honesty)+")")
    elif s.lower() == "comedy":
        Comedy = Comedy + v
        sys.stdout.write(" ("+str(Comedy)+")")
    elif s.lower() == "manipulation":
        Manipulation = Manipulation + v
        sys.stdout.write(" ("+str(Manipulation)+")")
    elif s.lower() == "bravery":
        Bravery = Bravery + v
        sys.stdout.write(" ("+str(Bravery)+")")
    else:
        DoError1()

    print(TextColor + '')

def Action(s):
    global actioncharacter
    global typetime

    print(' ')
    s1 = actioncharacter + " " + s + " " + actioncharacter

    for c in s1:
        sys.stdout.write(ActionColor + c)
        sys.stdout.flush()
        time.sleep(typetime)
    print('')



def Speak(s,v):
    global Type
    global WaitTimeBetweenSentence
    global Speaker
    global SpeakType
    global PlayerColor
    global CharacterColor
    global typetime
    global TextColor

    print('')
    
    if SpeakType == "NPC":
        sys.stdout.write(CharacterColor +Speaker + ": ")
    elif SpeakType == "PLR":
        sys.stdout.write(PlayerColor + Speaker + ": ")

    wait(WaitTimeBetweenSentence)

    for c in s:
        playsound('AudioFiles\\talking.mp3', block=False)
        sys.stdout.write(TextColor + c)
        sys.stdout.flush()
        time.sleep(typetime)

    if v == 1:
        print('')