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
PlayerColor = colorama.Fore.CYAN
CharacterColor = colorama.Fore.RED
ChoiceMenuColor = colorama.Fore.GREEN
TextColor = colorama.Fore.WHITE

#Functions

def end():
    active = False
    quit()

def wait(time):
    time.sleep(time)

def sp(s,s2,v):
        global typetime
        global CharacterColor

        sys.stdout.write(CharacterColor + s + " ")

        for c in s2:
            sys.stdout.write(TextColor + c)
            sys.stdout.flush()
            time.sleep(typetime)

        if v == "+":
            print('')

while(active == True):
    sp("???:","Hey!","+")
    sp("???:","You there??","+")
    sp("???:","Wake up!","+")
    end()

    
    
    
    
    





