#Modules

from Variables import *
import time,random,os,colorama,sys,pyaudio,wave,keyboard,webbrowser,string,winsound
from ast import NameConstant
from operator import truediv
from unicodedata import name
from turtle import clearscreen
from tokenize import Name
from threading import Thread
from playsound import playsound
from pynput.keyboard import Key, Listener

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

slimecount = 0
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

#Usables

def dots():
    Sentence = ""
    for i in range(5):
        ClearScreen()
        Sentence = Sentence + "."
        if Sentence == "....":
            Sentence = "."
            time.sleep(1)
        EventWrite(Sentence)

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
    global result

    ChoiceMenuRun = True
    while ChoiceMenuRun == True:
        print('')
        print(ChoiceMenuColor + "a)",s)
        print(ChoiceMenuColor + "b)",s1)
        print(TextColor)
        result = 1
        t = Thread(target=inputsound)
        t.start()
        answer = input().lower()
        result = 0
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
        if s2 == "An adventurer (SLIME ESSENCE NEEDED)":
            print(ErrorColor + "c)",s2)
        else:
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

def getCode(length = 10, char = string.ascii_uppercase +
                          string.digits +           
                          string.ascii_lowercase ):
    return ''.join(random.choice( char) for x in range(length))

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

def EventWrite(s):
    global DeathColor
    print('')
    playsound('AudioFiles\\talking.mp3', block=False)
    for c in s:
        sys.stdout.write(EventColor + c)
        sys.stdout.flush()
        time.sleep(typetime / 2)

def death(s):
    global DeathColor
    print('')
    for c in s:
        playsound('AudioFiles\\playertalking.mp3', block=False)
        sys.stdout.write(DeathColor + c)
        sys.stdout.flush()
        time.sleep(typetime)

def death2(s):
    global DeathColor
    print('')
    for c in s:
        playsound('AudioFiles\\playertalking.mp3', block=False)
        sys.stdout.write(DeathColor + c)
        sys.stdout.flush()
        time.sleep(typetime / 10)

def playagain():
    global Name
    global Manipulation
    global Bravery
    global Comedy
    global Honesty
    answer = ""
    while answer != "n" or answer != "y":
        death("Play again? y/n")
        x = input().lower()
        if x == "y":
            Comedy = 0
            Bravery = 0
            Honesty = 0
            Manipulation = 0
            Name = ""
            ClearScreen()
            death("Loading..")
            time.sleep(2)
            Start()
        elif x == "n":
            end()
            quit()

def Battle(Entity,givenmessage):
    global slimecount
    global PlrLvl
    global Name
    global PlrHP
    global inventory
    chance = 2
    ClearScreen()
    EventWrite("A "+str(Entity)+" appeared!")
    time.sleep(2)
    if Entity == "Slime":
        ClearScreen()
        MaxHP = 5
        MaxPlrHP = PlrHP
        HP = 5

        while HP > 0:
            if PlrHP > 0:
                ClearScreen()
                print('')
                EventWrite("Slime")
                EventWrite("Level: 1")
                EventWrite("HP: "+str(HP)+"/"+str(MaxHP))
                print('')
                EventWrite(Name)
                EventWrite("Level: "+str(PlrLvl))
                EventWrite("Hp: "+str(PlrHP)+"/"+str(MaxPlrHP))
                print('')
                x = ChoiceMenu2("Punch","Cry")
                if x == "b":
                    EventWrite("You broke down into tears and confused the slime")
                    death("The slime has lost accuracy by -1!")
                elif x == "a":
                    crit = random.randint(1,3)
                    if crit == 1:
                        death("Critical hit!")
                        Damage = 4 + PlrLvl
                        HP = HP - Damage
                        EventWrite("You punched the slime and dealt "+str(Damage)+" damage!")
                    else:
                        miss = random.randint(1,5)
                        if miss == 1:
                            death("You missed!")
                        else:
                            Damage = 2 + PlrLvl
                            HP = HP - Damage
                            EventWrite("You punched the slime and dealt "+str(Damage)+" damage!")
                    if HP > 0:
                        slimeattack = random.randint(1,chance)
                        if slimeattack == 1:
                            EventWrite("The slime attacked and dealt 2 damage!")
                            PlrHP = PlrHP - 2
                    time.sleep(2)
            else:
                dumbending()
        print('')
        EventWrite("You beat the Slime!")
        EventWrite("You've obtained Slime Essence!")
        EventWrite("You've gained one level!")
        PlrLvl = PlrLvl + 1
        inventory.append("SlimeEssence")
        ClearScreen()
        if givenmessage == "firstencounter":
            AfterSlime()
        elif givenmessage == "five":
            slimecount = slimecount + 1
            PlrHP = MaxPlrHP
            if slimecount == 5:
                DefeatedFiveSlimes()
            else:
                ClearScreen()
                Action("You continue to roam around in search of slimes...")
                time.sleep(random.randint(1,5))
                Battle("Slime","five")
        elif givenmessage.lower() == "identify3":
            Battle("Dragon")
    elif Entity == "Dragon":
        if givenmessage.lower() == "ending":
            PlrLvl = 9999
            PlrHP = 69420
        ClearScreen()
        MaxHP = 500
        MaxPlrHP = PlrHP
        HP = 500

        while HP > 0:
            if PlrHP > 0:
                ClearScreen()
                print('')
                EventWrite("Dragon")
                EventWrite("Level: 69")
                EventWrite("HP: "+str(HP)+"/"+str(MaxHP))
                print('')
                EventWrite(Name)
                EventWrite("Level: "+str(PlrLvl))
                EventWrite("Hp: "+str(PlrHP)+"/"+str(MaxPlrHP))
                print('')
                x = ChoiceMenu2("Punch","Cry")
                if x == "b":
                    EventWrite("You broke down into tears and confused the dragon")
                    death("The dragon has lost accuracy by -1!")
                elif x == "a":
                    crit = random.randint(1,3)
                    if crit == 1:
                        death("CRITICAL HIT!")
                        Damage = 2 + PlrLvl
                        HP = HP - Damage
                        EventWrite("You punched the dragon and dealt "+str(Damage)+" damage!")
                    else:
                        miss = random.randint(1,5)
                        if miss == 1:
                            death("You missed!")
                        else:
                            Damage = 2 + PlrLvl
                            HP = HP - Damage
                            EventWrite("You punched the dragon and dealt "+str(Damage)+" damage!")
                    if HP > 0:
                        slimeattack = random.randint(1,chance)
                        if slimeattack == 1:
                            EventWrite("The dragon attacked and dealt 420 damage!")
                            PlrHP = PlrHP - 420
                    time.sleep(2)
            else:
                dragonslayentending()
        print('')
        GoodEnding()

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
        sys.stdout.write(CharacterColor + Speaker + ": ")
    elif SpeakType == "PLR":
        sys.stdout.write(PlayerColor + Speaker + ": ")
    elif SpeakType == "GOD":
        sys.stdout.write(GodColor + Speaker + ": ")

    wait(WaitTimeBetweenSentence)

    for c in s:
            
        if SpeakType == "PLR":
            playsound('AudioFiles\\playertalking.mp3', block=False)
        elif SpeakType == "NPC":
            playsound('AudioFiles\\talking.mp3', block=False)
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
        print('')
    result = 0

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

#Endings

def BunkerEnding():
    EventWrite("By being a pussy you waited off for the dragon to be slayed")
    EventWrite("The pussy ending")
    EventWrite("Seriously why")
    playagain()
    
def HoodedFigureEnding():
    death("The bunker door is forced open")
    death("You see the hooded figure you passed earlier standing in the opening")
    death("He walks over to you and stabs you in the gut")
    death("The bunker roof is torn off and as you lie on the ground you see the dragon's red glowing eyes looking at you from above")
    death("The mysterious figure ending")
    playagain()

def glitch():
    while True:
        original = "A̶̘̣̠̯̾̔̓͒̊̊͋̕B̷̳͉͖͉̱́́C̸̨̢̪̠̰͚͉̻̓̉̊̊̊̽́̚D̵̡͒͊Ê̷̪̚͝͠F̵̝̝̻͈͕́̎̚G̴̡̡̛͇͔͔̩̱̏͂̾̽̋̿̊͋H̸͉̿̏̅͊̄̋͘͘͠I̴̧̳͉̝͎̫̫͇͆̒͒̂͑͘̕J̴̡̮̯̥͎̜̺̈͛̓͗́̀̍Ḱ̶̨̛͚͚̯̮̺͔͕̔̎͐́͌̕̕L̸̪̳̀̓͌͠M̸̧̭̩̪̲̘̜͙̄͌͜Ņ̵̯͖̥̙̼͖͂͌͂̔͝Ǫ̵̨͉͕͔͎͙̣̋̂͆P̶͖̟̼̫̬̔̽̽Q̴̡͍̤͓͎͆͗͒͜R̵̢̺̼̺̳̭͍̐̀͌̎̓͜͠Ş̵̨͚͚̎̔͐̏̓̕͜͝͝Ť̴̫̎̈́U̴̧̡͙̗̰̟͖̟̥͗̈́̈͑̄̈V̵̨̢͔̞̞̱̲̔̓W̵̺̆̾̀͊ͅX̵͇̖̪̬͙͖͚̲̌̆̓̂͛͛͋̓͜Y̵̨͉̯̠͆͝Z̶̡̝̼̩̙̹̪̞̋̋"
        randomised = ''.join(random.sample(original, len(original)))
        
        death2(randomised)

def dumbending():
    death("You try desperately but lack the strength to do so..")
    death("The slime continues to feast on your arm and due to your new fragile body it succeeds to cause serious injury")
    death("You died due to slime absorbtion.")
    ClearScreen()
    time.sleep(1)
    death("The dumb ending")
    playagain()

def GodEnding():
    global typetime
    oldtypetime = typetime
    EventWrite("* You pick up the ring and feel an extreme power surging through your veins *")
    typetime = 0.003
    for i in range(random.randint(50,100)):
        n = random.randint(1,4)
        if n == 1:
            Event("Honesty",420)
        elif n == 2:
            Event("Manipulation",420)
        elif n == 3:
            Event("Comedy",420)
        elif n == 4:
            Event("Bravery",420)
    time.sleep(random.randint(1,3))
    typetime = oldtypetime
    EventWrite("You've obtained godlike powers and no longer feel pressure from the dragon")
    EventWrite("You grow wings and feel stronger than you've ever been")
    Battle("Dragon","Ending")

def dragonslayentending():
    death("As expected the dragon was far stronger")
    death("You died")
    death("The dragon slayen't ending")
    playagain()

def GoodEnding():
    EventWrite("You somehow managed to kill the dragon!")
    EventWrite("Slay?")
    EventWrite("You beat the dragon!")
    EventWrite("You've obtained Legendary Excalibur!")
    EventWrite("You've obtained Legendary Dragon Scales!")
    EventWrite("You've obtained Legendary Skills!")
    EventWrite("You've obtained The title Dragon Slayer!")
    EventWrite("You've obtained The title Hero!")
    inventory.append("Excalibur")
    inventory.append("Dragon Scales")
    inventory.append("TDragon_Slayer")
    inventory.append("THero")
    time.sleep(4)
    ClearScreen()
    EventWrite("You became the most powerful person in this world.")
    EventWrite("The good ending!")
    playagain()

def BetrayalEnding():
    death("The betrayal ending")
    playagain()

def RunFromDragonEnding():
    Action("You attempt to run from the dragon")
    death("The dragon manifests a ball of energy and hits you with it")
    death("You died")
    playagain()

#Story

def Start(): #One
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

def StartTwo(): #Two
    global Name
    global Manipulation
    global Bravery
    global Comedy
    global Honesty
    ChangeSpeaker("???")
    ChangeSpeakerType("NPC")
    Speak("Either way, we have to go right now.",1)
    Speak("By the way, what's your name?",2)
    Speak("Ahh, that's a cool name!",1)
    ChangeSpeaker("Yuki")
    Speak("My name is Yuki!",1)
    Speak("Nice to meet you",3)
    Speak("Okay, we have to go, there's soldiers on our tail!",1)
    Action(Name + " and Yuki start running")
    time.sleep(2)
    ChangeSpeaker("Soldier")
    Speak("STOP RIGHT THERE!!",1)
    Action("Bullets fly toward you at an incredible speed")
    ChangeSpeaker("Yuki")
    Speak("RUN!!",1)
    time.sleep(2)
    Action("You feel three bullets puncture your body as you fall down on the ground")
    Speak(Name+"!",1)
    Action("You feel cold")
    Speak(Name.upper()+"!!",1)
    Action("However you also feel warm")
    Action("You're in pain however still very comfortable")
    Action("Everything fades to black however the color also resembles white")
    ChangeSpeaker(Name)
    ChangeSpeakerType("PLR")
    Speak("What's happening..",1)
    time.sleep(1)
    Speak("Am I dead?",1)
    time.sleep(1)
    Speak("Did I die?",1)
    time.sleep(1)
    Speak("I got shot.",1)
    time.sleep(1)
    Speak("Yuki?",1)
    time.sleep(3)
    ClearScreen()
    time.sleep(1)
    NewWorld()

def NewWorld(): #Three
    global Name
    global Manipulation
    global Bravery
    global Comedy
    global Honesty
    Speak("I died..",1)
    time.sleep(3)
    Speak("I can still feel my body..",1)
    Action("You try to open your eyes")
    Speak("!!!",1)
    Speak("What's this??",1)
    Action("You find yourself laying under a tree in a grass valley")
    Speak("What..?",1)
    Speak("I feel.. Different",1)
    Action("You look up at the sky and realize there are two planets you don't recognize")
    Speak("What?",1)
    Action("You feel a slimey texture on ur arm and turn to face it")
    Speak("A SLIME?!",1)
    Speak("WHAT SHOULD I DO?!",1)
    x = ChoiceMenu2("Run away","Fight it")
    if x == "a":
        Event("Honesty",3)
        Action("You run away far into the grasslands")
        Action("The slime lets go as soon as you start running fast enough.")
        AfterSlime()
    elif x == "b":
        Event("Bravery",3)
        Action("You flail your arms around like a kitten getting picked up and cry tears of disgust and fear")
        Action("The slime lets go of your arm not due to your strength but due to pure fear of the stupidness of ur decision.")
        Event("Comedy",3)
        Battle("Slime","firstencounter")

def AfterSlime(): #Four
    Action("You realize there's not much to see from here.")
    x = ChoiceMenu2("Search for a village","Stay here")
    if x == "a":
        SearchVillage()
    elif x == "b":
        Action("You decided to wait it out")
        time.sleep(random.randint(1,8))
        Battle("Dragon","a")

def SearchVillage(): #Five
    global Name
    global inventory
    Action("You killed the slime and started walking in search for anything that isn't just grasslands")
    Action("After three hours of walking you stumble upon a village")
    Action("It seems to be guarded, however you've already come so far. No turning back now.")
    Action("You walk up to the village entrance.")
    ChangeSpeakerType("NPC")
    ChangeSpeaker("Guard")
    Halt()

def Halt(): #Six
    global inventory
    Speak("HALT!",1)
    Speak("Who are you?",1)
    if "SlimeEssence" in inventory:
        x = ChoiceMenu3("I don't know","Where am I?","An adventurer (Slime Essence)")
    else:
        x = ChoiceMenu3("I don't know","Where am I?","An adventurer (SLIME ESSENCE NEEDED)")
    ChangeSpeakerType("PLR")
    ChangeSpeaker(Name)
    if x == "a":
        Speak("I don't know.",1)
        Event("Honesty",3)
        ChangeSpeakerType("NPC")
        ChangeSpeaker("Guard")
        HonestChoice()
    elif x == "b":
        Speak("Where am I?",1)
        Event("Bravery",2)
        Event("Honesty",2)
        ChangeSpeakerType("NPC")
        ChangeSpeaker("Guard")
        ShowLocation()
    elif x == "c":
        if "SlimeEssence" in inventory:
            Speak("An adventurer",1)
            Action("You show the slime essence as proof of ur skill")
            Event("Bravery",3)
            Event("Honesty",3)
            Event("Manipulation",3)
            ChangeSpeakerType("NPC")
            ChangeSpeaker("Guard")
            AdventurerChoice()
        else:
            Halt()

def HonestChoice(): #SevenA
    Speak("so you're lost.. Well you're in zeldom village now pal",1)
    ShowLocation()

def ShowLocation(): #SevenB
    Speak("Ahh what the heck, I'll show you around.",1)
    Speak("Switch!",1)
    Action("A different guard comes running up from behind a building and switches places with the guard you're talking to")
    time.sleep(2)
    Action("The guard escorts you into the village and shows you around")
    Action("You end up in front of the adventurers guild")
    Speak("All the people entering and leaving this village are usually either merchants or adventurers. Would you like to become an adventurer?",1)
    x = ChoiceMenu2("yes","nah fam im good")
    if x == "a":
        AdventurersGuild()
    elif x == "b":
        ContinueTown()

def AdventurerChoice(): #SevenC
    Speak("Ahh, an adventurer!",1)
    Speak("Killing mere slimes?",1)
    Action("The guard lets out a cringeworthingly loud laugh")
    Speak("Let me show you around kid!",1)
    Action("You follow the guard.")
    Speak("This is the adventurers guild, let's go inside!",1)
    AdventurersGuild()

def ContinueTown(): #Eight1
    Action("The guard continues to take you around")
    Action("You end up in front of the gay bar")
    Speak("Would you like to become a gay?",1)
    x = ChoiceMenu2("yass queeennn slayyyyy pop that pussyyy!! yassssssss material gwrolll"," I like boobi.")
    if x == "a":
        DatingSim1()
    elif x == "b":
        ContinueTown2()

def DatingSim1(): #NineA
    global Name
    ClearScreen()
    Date = random.choice(DatingList)
    Action("You enter the gay bar")
    ChangeSpeakerType("NPC")
    ChangeSpeaker(Date)
    Speak("Hey, I haven't seen you around before",1)
    Speak("You new here?",1)
    ChangeSpeakerType("PLR")
    ChangeSpeaker(Name)
    Speak("Yea.",1)
    ChangeSpeakerType("NPC")
    ChangeSpeaker(Date)
    Speak("You want a drink?",1)
    x = ChoiceMenu2("Yes","No")
    if x == "a":
        DatingSim2(Date)
    elif x == "b":
        death("You got beat up by "+Date+" for rejecting them.")
        BetrayalEnding()

def DatingSim2(Date): #NineA2
    Action("You continue to chat and enjoy drinks throughout the evening")
    Action("You forget about the war and enjoy ur reincarnated gay life with "+Date)
    EventWrite("The gay ending")
    playagain()

def ContinueTown2(): #NineB
    Action("The guard brings you to the torture dungeons")
    death2("Ý̶̡̛̟̠̭͊̎̓̂̈́͑͝ơ̶̼̭͖̓͑͗̈́́̔ǔ̶̝̿̾̈́̀̕ ̷̲̦̖̗̠͚͋͊̐̾f̸̢̘͍̘̱̜̙̪̗̔̄̀̑̈́̀͑̔͠͠a̶̧̘̙̱̤̱̮͋͗̃̽͒̈́̂̈̽́̉̇͘̕̚ͅi̷̼̬̗͔̪̒̔̑̍̀̚ͅļ̶͔͔̠̻̫͓̺̐͗̊͋͘͠͝e̸̮̝͇̲̲͙͈̮̮̖̱̲͋̀̇́̐̏̒̆͘ͅḏ̴̽̽̒̔͐͆̓̍́̾̆̋̕ͅ")
    death2("* ThE GUARD K̸̛̤͋͒͐̌̅͊̔͘͠͝Ỉ̶̠̆̍̋̇L̶̳̖̰̰̝̻̹̜̰̲̮̉̄̓͗͝L̴͙̇̈͌̆̌͌͒̉̈̋̓̕͝͝S̶̨̨̧̡̩̖̳͚͓̝͇̗̼͛̈́̀́̃́͐͂͑ ̷̢̦̖̙̃͗̓͐̈́͐͗͐͗̚̕͝Y̴̡̋͝O̵̖̘̜̤̫͋͌̅̂͗́̑̏U̵̧̜̣̣͉̍̑̋̌̉͒̆̀̏")
    glitch()

def AdventurersGuild(): #Eight2
    global Name
    global inventory
    Action("You and the guard enter the adventurers guild")
    Speak("This is the adventurers guild! Isn't it beautiful!",1)
    Action("The adventurers guild building was relatively small on the outside but upon entering you find yourself in a huge cave connecting to different sections.")
    Speak("Let's go to the front desk",1)
    Action("You walk to the front desk")
    ChangeSpeaker("Front desk helper")
    Speak("Hello! How may I help you?",1)
    ChangeSpeaker(Name)
    ChangeSpeakerType("PLR")
    answer = ""
    while answer != "a":
        x = ChoiceMenu2("Register as an adventurer","Leave")
        if x == "a":
            answer = x
            Speak("I'd like to register as an adventurer please.",1)
            ChangeSpeaker("Front desk helper")
            ChangeSpeakerType("NPC")
            Speak("Alright! Give me a second..",1)
            time.sleep(4)
            Speak("All set! Here's your Adventurers Pass!",1)
            EventWrite("Obtained Adventurers Pass")
            inventory.append("AdventurersPass")
            Speak("Alright, we currently have two quests. Pick one!",1)
            x = ChoiceMenu2("Defeat five slimes in the grasslands","Identify three different creatures in the grasslands")
            ChangeSpeaker(Name)
            ChangeSpeakerType("PLR")
            if x == "a":
                Speak("I'll do the quest: Defeat five slimes in the grasslands",1)
                ChangeSpeaker("Front desk helper")
                ChangeSpeakerType("NPC")
                DefeatFiveSlimes()
            elif x == "b":
                Speak("Identify three different creatures in the grasslands",1)
                ChangeSpeaker("Front desk helper")
                ChangeSpeakerType("NPC")
                IdentifyThree()
        elif x == "b":
            Action("The pressure isn't allowing you to leave.")

def DefeatFiveSlimes(): #Nine2A
    Battle("Slime","five")

def IdentifyThree(): #Nine2B
    Battle("Slime","Identify3")

def DefeatedFiveSlimes(): #Ten2
    global PlrLvl
    Action("You go back to the adventurers guild to show your acomplishment")
    ChangeSpeakerType("NPC")
    ChangeSpeaker("Front Desk Helper")
    Speak("Nice! It seems you've defeated five slimes succesfully and grown to level "+str(PlrLvl)+"!",1)
    Speak("Would you like to take this quest again?",1)
    x = ChoiceMenu2("Take the quest again","Continue the story")
    if x == "a":
        ChangeSpeakerType("PLR")
        ChangeSpeaker(Name)
        Speak("I'd like to grow stronger and take the quest again.",1)
        DefeatFiveSlimes()
    elif x == "b":
        ContinueAdventure()

def ContinueAdventure(): #Eleven
    Speak("Alright from now on you'-",1)
    Action("The entire building starts shaking")
    Speak("What's that??",1)
    ClearScreen()
    Action("Somebody burts through the door")
    ChangeSpeaker("Guard")
    Speak("DRAGON!!",1)
    Speak("EVERYBODY EVACUATE!",1)
    x = ChoiceMenu2("Evacuate","Go seek the dragon")
    if x == "a":
        Evacuate()
    elif x == "b":
        SeekDragon()

def Evacuate(): #TwelveA
    Speak("LET'S GO!!",1)
    time.sleep(0.5)
    ClearScreen()
    Action("You follow the guard into the town bunker")
    Speak("GO, RUN!",1)
    Action("You hear the guard screaming in pain from behind you")
    x = ChoiceMenu2("Go back for the guard","Continue running")
    if x == "a":
        Action("You go back to try and save the guard")
        dragonslayentending()
    elif x == "b":
        ContinueRunning()
    
def SeekDragon(): #TwelveB
    Action("You run past the guard to go outside and find the dragon")
    Event("bravery",3)
    Speak("HEY!! WHERE ARE YOU GOING?!",1)
    time.sleep(0.5)
    ClearScreen()
    ChangeSpeaker(Name)
    ChangeSpeakerType("PLR")
    Speak("I don't even know what I'm doing",1)
    Speak("After killing those slimes I felt something tho..",1)
    Speak("A certain power",1)
    Speak("A power to protect me from danger",1)
    Action("You get to the dragon, seeing a mere scratch on its head and all the people fighting it either knocked out or dead on the ground")
    Speak("I...",1)
    Action("You lock eyes with the dragon")
    Action("It looks at you with a dissaranged look")
    x = ChoiceMenu2("Attempt to fight it","Run away")
    if x == "a":
        FightDragon()
    elif x == "b":
        RunFromDragonEnding()

def FightDragon(): #Thirteen2
    ClearScreen()
    dots()
    death("You feel an extremely dangerous aura making you unable to move")
    time.sleep(1)
    dots()
    time.sleep(2)
    x = ChoiceMenu2("Try to move", " Stand still")
    if x == "a":
        DragonTryToMove()
    elif x == "b":
        dragonslayentending()

def DragonTryToMove(): #Fourteen2A
    Action("You try to move")
    death("* The dragon looks at you in confusion *")
    Action("It doesn't work")
    time.sleep(1)
    ClearScreen()
    time.sleep(1)
    ChangeSpeaker("???")
    ChangeSpeakerType("GOD")
    Speak("VELDORA, TRUE DRAGON OF STORMS, FACE ME!",1)
    Action("The dragon changes its head towards the entity")
    Action("You're no longer stunned")
    Action("You turn around to look at the person talking, only to see a bright light and two enormous wings")
    Action("The winged entity seems to teleport towards the dragon and smites it with a beam of light")
    Action("The dragon doesn't seem to budge and bites the person.")
    death("The winged person is bit in half.")
    Action("The entity has dropped a mysterious golden ring")
    x = ChoiceMenu2("Pick it up and wear it","Leave it")
    if x == "a":
        GodEnding()
    elif x == "b":
        dragonslayentending()

def ContinueRunning(): #Thirteen1
    Action("You decide to continue running to the bunker")
    Action("A hooded figure with what seems to be a staff emitting red light stops you")
    x = ChoiceMenu2("Shove them away and continue running","Punch them in the face")
    if x == "a":
        ContinueRunning2()
    elif x == "b":
        HoodedFigureFight()

def ContinueRunning2(): #Thirteen1A
    Action("You shove the figure away and continue making your way to the bunker")
    Action("You finally make it to the bunker and the guards close the bunker door")
    time.sleep(1)
    ClearScreen()
    time.sleep(2)
    Action("Hours of silence pass")
    time.sleep(0.5)
    ClearScreen()
    Action("You hear an extremely loud noise and start feeling nauseous")
    Action("You start losing your vision and balance")
    HoodedFigureEnding()

def HoodedFigureFight(): #Thirteen1B
    Action("You punch the hooded figure in the face and continue running to the bunker")
    death("The hooded figure gets absolutely yeeted into a wall")
    Action("You get into the bunker and the guard closes the door")
    time.sleep(1)
    ClearScreen()
    time.sleep(1)
    Action("Hours pass")
    ChangeSpeaker("Guard")
    ChangeSpeakerType("NPC")
    Speak("THE DRAGON HAS BEEN SLAYED!",1)
    Action("Everybody cheers and the bunker is opened")
    BunkerEnding()
