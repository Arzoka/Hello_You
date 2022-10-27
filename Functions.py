#Modules

from operator import truediv
import time
import random
import os
from tokenize import Name
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
from Variables import StatColor
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
KeyPressed = ""

def on_press(key):
    global pressed
    global KeyPressed
    if pressed == False:
        if result == 1:
            playsound('AudioFiles\\typesound.mp3', block=False)
        pressed = True
    elif KeyPressed != key:
        if result == 1:
            playsound('AudioFiles\\typesound.mp3', block=False)
        pressed = True
    KeyPressed = key

def on_release(key):
    global pressed
    pressed = False

# Collect events until released

result = 0
Name = ""

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

def ShowStats():
    global Honesty
    global Manipulation
    global Comedy
    global Bravery
    global StatColor
    print(StatColor + "Honesty: " + str(Honesty))
    print(StatColor + "Manipulation: " + str(Manipulation))
    print(StatColor + "Comedy: " + str(Comedy))
    print(StatColor + "Bravery: " + str(Bravery))
    

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
    global Name
    global result

    print('')
    
    if SpeakType == "NPC":
        sys.stdout.write(CharacterColor +Speaker + ": ")
    elif SpeakType == "PLR":
        sys.stdout.write(PlayerColor + Speaker + ": ")

    wait(WaitTimeBetweenSentence)

    for c in s:
        if SpeakType == "NPC":
            playsound('AudioFiles\\talking.mp3', block=False)
        elif SpeakType == "PLR":
            playsound('AudioFiles\\playertalking.mp3', block=False)
        sys.stdout.write(TextColor + c)
        sys.stdout.flush()
        time.sleep(typetime)

    if v == 1:
        print('')
    elif v == 2:
        print('')
        print('')
        if Name == "":
            result = 1
            answer = input(PlayerColor + "Player" + ": " + TextColor)
            Name = answer
            return(answer)
        else:
            result = 1
            answer = input(PlayerColor + Name + ": " + TextColor)
            return(answer)
        print('')
    elif v == 3:
        Added = " "+Name+"!"
        for c in Added:
            sys.stdout.write(TextColor + c)
            sys.stdout.flush()
            playsound('AudioFiles\\talking.mp3', block=False)
            time.sleep(typetime)

def Start():
    ClearScreen()

    ChangeSpeaker("???")
    ChangeSpeakerType("NPC")

    Speak("Hey!",1)
    Speak("Are you there??",1)
    Speak("Wake up!",1)
    Speak("Hello??",1)

    Action("You wake up")

    Speak("Oh you're finally awake!",1)
    Speak("What happened to you?",1)

    x = ChoiceMenu3("I don't know","ur mom","I was sent by the gods to help you out")

    ChangeSpeaker("Player")
    ChangeSpeakerType("PLR")

    if x == "a":
        one_a()

    elif x == "b":
        one_b()
    
    elif x == "c":
        one_c()

def one_a():
    Speak("I... Don't know",1)
    Event("Honesty",3)
    StartTwo()

def one_b():
    Speak("ur mom",1)
    Event("Comedy",3)
    StartTwo()

def one_c():
    Speak("I was sent by the gods to help you out",1)
    Event("Manipulation",3)
    StartTwo()

def StartTwo():
    ChangeSpeaker("???")
    ChangeSpeakerType("NPC")
    Speak("Either way, we have to go!",1)
    Speak("By the way, what's your name?",2)
    Speak("Ahh, that's a cool name!",1)
    ChangeSpeaker("Yuki")
    Speak("My name is Yuki!",1)
    Speak("Nice to meet you",3)

    end()