#Modules

from operator import truediv
import time
import random
import os
import colorama
import sys

#Functions

from Functions import clearscreen
from Functions import speak
from Functions import wait
from Functions import end
from Functions import changespeaker

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

while(active == True):
    clearscreen()

    changespeaker("???")

    speak("Hey!",1)
    speak("You there!",1)
    speak("Wake up!",1)

    end()
