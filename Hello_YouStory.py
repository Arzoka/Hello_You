#Modules

from operator import truediv
import time
import random
import os
from colorama import Fore
import sys
from playsound import playsound

#Functions

from Functions import *

#StartCode

while True:
    ClearScreen()

    ChangeSpeaker("???")
    ChangeSpeakerType("NPC")

    Speak("Hey!",1)
    Speak("You there!",1)
    Speak("Wake up!",1)
    Speak("Hello??",1)

    Action("You wake up")

    Speak("Oh you're finally awake!",1)
    Speak("What happened to you?",1)

    x = ChoiceMenu3("I don't know","ur mom","I was sent to eradicate the human race")

    if x == "a":
        ChangeSpeaker("Player")
        ChangeSpeakerType("PLR")

        Speak("I... Don't know",1)

        Event("Honesty",3)

    end()