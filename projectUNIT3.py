########
#import modules
#######
### In this game i made it so you the player must navigate the house you got put into after getting kidnapped and you must find a way out and remeber to eat or else you would die of hunger if you do not eat
import time
import os
# This will trigger once the player dies and give choice to restart
def dead2():
    global hunger
    print ("you are now dead\n")
    move = input("what would you like to do\n\trestart\n\tstay dead\n")
    if move.lower() == ("restart"):
        hunger = 0
        start()
    elif move.lower() == ("stay dead"):
        print("now your actually dead")
    else:
        dead2()
    
# this the part when text appears then you die
def endgame():
    wipe()
    print ("you died due to lack of food, you should've eaten out of kitchen\n")
    dead2()
    
# this will replenish your hunger
def eat():
    global hunger
    hunger = 0 
    print("You've eaten some food")
    startingroom()


# makes the death function work?
def dead():
    wipe()
    print("you died, rip")
    endgame()
    
# responsible for the hunger mechnic
def check_hunger():
    os.system('clear')
    global hunger
    hunger = hunger + 1
    if hunger == 22:
        dead()
    else:
        print("your hunger is", 21 - hunger, "out of 20")
# little help for me to check on the certain part of the game without going through it myself several times
def cheat():
    global keyfragment1, keyfragment2, HaveChair
    keyfragment1 = True
    keyfragment2 = True
    HaveChair = True
    print ("you cheated congrats now leave")

    secrettunnel()
#clears users screen 
def wipe():
    os.system('clear')
#diffrent starting room for when you pick up the chair
def startingroom2():
    global hunger
    check_hunger()
    print("You are in StartingRoom")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tlibrary\n\tbedroom\n\tkitchen\n\tstay in Starting Room\n")
    if move.lower() == "library":
        library2()
    elif move.lower() == "bedroom":
        bedroom()
    elif move.lower() == "kitchen":
        Kitchen()
    elif move.lower == "stay in starting room":
        startingroom()
    else:
        print("\nWell, you didnt respond so ill guees you want to remain here.")
        startingroom2()
#the Kitchen (used for eating)
def kitchen():
    global hunger
    check_hunger()
    print ("You have entered the kitchen seems like your hungry you should eat some food")
    move = input("\nWhat would you like to do\n\teat\n")
    if move.lower() == ("eat"):
        print ("It seems you are now full and you go back to the starting room")
        eat()
    else:
        kitchen()
        
#the secret room in which you need to open the door to win the game    
def secretroom():
    global keyfragment1, keyfragment2, hunger
    check_hunger()
    print ("you have entered the secert room and you notice the door has a lock on it\n")
    move = input("\nwhat do you do?\n\tinsert key\n\tgo back\n")
    if move.lower() == ("insert key"):
        if keyfragment1 == True and keyfragment2 == True:
            wipe()
            print("Congrats you escaped the house and have earned your freedom")
            print ('''                    ________$$$$
                    _______$$__$
                    _______$___$$
                    _______$___$$
                    _______$$___$$
                    ________$____$$
                    ________$$____$$$
                    _________$$_____$$
                    _________$$______$$
                    __________$_______$$
                    ____$$$$$$$________$$
                    __$$$_______________$$$$$$
                    _$$____$$$$____________$$$
                    _$___$$$__$$$____________$$
                    _$$________$$$____________$
                    __$$____$$$$$$____________$
                    __$$$$$$$____$$___________$
                    __$$_______$$$$___________$
                    ___$$$$$$$$$__$$_________$$
                    ____$________$$$$_____$$$$
                    ____$$____$$$$$$____$$$$$$
                    _____$$$$$$____$$__$$
                    _______$_____$$$_$$$
                    ________$$$$$$$$$$''')
                

#the first obsticle in which the user must have picked up the chair in order to progress due to there being a glass door halting their progress
def secrettunnel():
    global HaveChair
    check_hunger()
    print ("you appear to find your self in qute a long hallway as you walk down the dim hallway you stumble into a pretty thick glass door you cant seem to break it with your bare fists perhaps you need some sort of item to break the glass door that seems to lead to\nanother pretty empty room with a door in it")
    move = input("\nwhat do you do\n\tbreak it\n\trun back out to the bedroom\n")
    if move.lower() == ("break it"):
        if HaveChair == True:
            print ("It worked ")
            secretroom()
        else:
            print("it seems you've yet to find an item to break open the glass door")
            secrettunnel()
    elif move.lower() == ("run back out to the bedroom"):
        bedroom()
#inside the cabinet when you turn the dorrknob you go to secret tunnel
def insidecabinet():
    check_hunger()
    print ("\nyou are inside the cabinet now\nyou feel around the inside of the cabinet for anything and you feel a doorknob")
    move = input("\nwhat do you do?\n\tturn the doorknob\n\tleave\n")
    if move.lower() == ("turn the doorknob"):
        secrettunnel()
    elif move.lower() == ("leave"):
        bedroom()
#to open the cabinet or go back
def cabinet():
    check_hunger()
    print("your at the cabinet")
    move = input('\nyour infront of the tall cabinet what do you do?\n\topen it\n\tleave\n')
    if move.lower() == ("open it"):
        print('you opened it and walked inside the big cabinet')
        insidecabinet()
#diffrent library in which there is no chair because you picked up the chair
def library2():
    check_hunger()
    print("You are in Library")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tstarting room\n")
    if move.lower() == "starting room":
        startingroom2()
    else:
        library2()
        pass
#the drawer in which you find one of the key fragments
def drawer():
    global keyfragment2, hunger
    check_hunger()
    print ("your at the drawers")
    move = input("\nwhat would you like to do\n\topen drawer1\n\topen drawer2\n\topen drawer3\n\tleave\n")
    if move.lower() == ("open drawer1"):
        print ("nothing here")
        drawer()

    elif move.lower() == ("open drawer2"):
        keyfragment2 = True
        print ("seems to be a piece of a key")
        drawer()

    elif move.lower() == ("open drawer3"):
        print ("nothing here")
        drawer()
    elif move.lower()== ("leave"):
        bedroom()
#another interactable objdect where you'll find another key fragment
def bed():
    global keyfragment1, hunger
    check_hunger
    print ("\nyour at the bed")
    move = input("\n would you like to\n\tcheck covers\n\tcheck pillow\n\tleave bed\n")
    if move.lower()==('leave bed'):
        bedroom()
    elif move.lower()==("check covers"):
        time.sleep(2)
        print("nothing here")
        bed()
    elif move.lower() == ("check pillow"):
        keyfragment1 = True
        print("you've found a key fragment maybe useful later but still seems to be missing a piece")
        bed()    


# you st on the chair and have a choice to pick it up
def sit():
    global HaveChair, NoChair
    check_hunger()
    print("\nYour sitting now")
    move = input("\nWhat would you like to do? say any of these choices:\n\tkeep sitting\n\tgrab chair\n")
    if move.lower() == "keep sitting":
        sit()
    elif move.lower() == "grab chair":
        HaveChair = True
        NoChair = False
        print ('\nYou have grabbed the chair')
        library2()
       
# the start of the game
def start():
    global hunger
    check_hunger()
    print("Welcome!")
    print("You just got kidnapped and have to find a way out the house.")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tlibrary\n\tbedroom\n\tkitchen\n\tstay\n")
    if move.lower() == "library":
        library()
    elif move.lower() == "bedroom":
        bedroom()
    elif move.lower() == "kitchen":
        kitchen()
    elif move.lower() == "stay":
        startingroom()
    elif move.lower() == ("cheat"):
        cheat()
    else:
        print("\nWell, you didnt respond so ill guees you want to remain here.")
        time.sleep(1)
        startingroom()
#the first room (starting room) and gives you acess to 3 diffrent rooms
def startingroom():
    global hunger
    check_hunger()
    print("You are in StartingRoom")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tlibrary\n\tbedroom\n\tkitchen\n\tstay in Starting Room\n")
    if move.lower() == "library":
        library()
    elif move.lower() == "bedroom":
        bedroom()
    elif move.lower() == "kitchen":
        kitchen()
    elif move.lower == "stay in starting Room":
        startingroom()
    else:
        print("\nWell, you didnt respond so ill guees you want to remain here.")
        startingroom()
#the 2nd room (library) in which this is the place you get the chair
def library():
    check_hunger()
    print("You are in Library")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tStartingRoom\n\tSit\n")
    if move.lower() == "starting room":
        startingroom()
    elif move.lower() == "sit":
        sit()
    else:
        library()
        pass
#you can look through the cabinet,bed or drawer to find key frafgments and a secret entrance
def bedroom():
    check_hunger()
    print("You are in the bedroom")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tcheck bed\n\tcheck drawer\n\tcheck cabinet\n\tstarting room\n")
    if move.lower() == "check bed":
        bed()
    elif move.lower() == ("starting room"):
        startingroom()
    elif move.lower() == ("check drawer"):
        drawer()
    elif move.lower() == ("check cabinet"):
        cabinet()
    else:
        bedroom()
        pass


########
#main
#######
#TODO: Add some global variables
#main items player needs to progress
HaveChair = False
hunger = 0
keyfragment1 = False
keyfragment2 = False
#this will start the game
start()

###############
########