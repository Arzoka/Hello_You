#Modules

from operator import truediv
import time
import random
import os
from colorama import Fore
import sys

#Functions

from Functions import clearscreen
from Functions import speak
from Functions import wait
from Functions import end
from Functions import changespeaker

#StartCode

running = True

while(running == True):
    clearscreen()

    changespeaker("???")

    speak("Hey!",1)
    speak("You there!",1)
    speak("Wake up!",1)

    end()
