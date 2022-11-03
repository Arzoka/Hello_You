from traceback import format_exc
from colorama import Fore

#Color

PlayerColor = Fore.CYAN
CharacterColor = Fore.RED
ChoiceMenuColor = Fore.GREEN
TextColor = Fore.WHITE
EventColor = Fore.LIGHTMAGENTA_EX
StatColor = Fore.LIGHTMAGENTA_EX
ActionColor = Fore.YELLOW
ErrorColor = Fore.RED
DeathColor = Fore.RED
GodColor = Fore.YELLOW

#Timing

typetime = 0.06
WaitTimeBetweenSentence = 0.3

#Dialogue

actioncharacter = "*"

#Errors

Error1 = "ERROR 1: Event stat not found." #Event error
Error2 = "ERROR 2: Choice not found." #Choice menu error
Error3 = "ERROR 3: Code broke, cause unknown." #Code breaking

#Stats

Honesty = 0
slimecount = 0
result = 0
Manipulation = 0
Comedy = 0
Bravery = 0
PlrHP = 25
PlrLvl = 1
inventory = ["SlimeEssence"]
Name = ""

#Code

holding = False
pressed = False
KeyPressed = ""

#DatingSim
DatingList = ["Jeff Satur","Johnny Depp","Lan Zhan","Wei Wuxian","Bible Sumett"]