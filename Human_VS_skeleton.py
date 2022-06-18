#classpractice
# helpful : https://www.youtube.com/watch?v=rJzjDszODTI
from unittest.loader import VALID_MODULE_NAME
import random
from os import system, name
import os

if name == 'nt':
    os.system('cls')
  
    # for mac and linux(here, os.name is 'posix')
else:
    os.system('clear')


## -- Main Logic -- ##

print('Welcome to Skeleton VS Human, press any key to continue - The game starts on level 2 cause level 1 sucks')

def mainlogic():
    
    ## bad logic ##
    #next_level = level + 1
    #print('level:', next_level)


    statement = input().lower()
    if skeleton.hp < 0:
        skeleton.hp = 150
    if Human.hp < 0:
        Human.hp = 175



    while True:
        print('What would you like to do? a) Attack skeleton b) Run From Monster\n')

        if statement == 'a':
            Human.attack()
            skeleton.attack(1)
            lifecheck()
        elif statement == 'b':
            print(" -- Out of skeleton's reach, skeleton + 10 hp --")
            skeleton.attack(0)
            skeleton.hp = skeleton.hp + 10
            print('skeleton HP: ' , skeleton.hp)

            lifecheck()

        
        statement = input().lower()
        clear()



def clear():
  
    # for windows
    if name == 'nt':
        os.system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')

## -- Monster ----------------------------------------------------##
##game globals




class Monster:
    def __init__(self, age, hp, attack_damage):
        self.age = age
        self.hp = hp
        self.attack_damage = attack_damage

## -- extra functions --##
    def walk(self):
        print("walking...")
    def run(self):
        print("running...")

## -- run damage negate -- ##
    def attack(self, damage):
        if damage == 0:
            damage = 0
        else:
# -- damage component -- ##
            skeleton.hp = skeleton.hp 
            damage = skeleton.attack_damage 
            #damage = random.randrange(15,25) + level

        ## -- crithit ranodm roll -- ##
            unluck1 = random.randrange(0,4)
            unluck2 = random.randrange(0,4)
            if unluck1 == unluck2:
                damage = damage*2
                print(' -- Double Damage! -- ')

        ## health up random roll ##
            unluck1 = random.randrange(0,5)
            unluck2 = random.randrange(0,8)
            if unluck1 == unluck2:
                skeleton.hp = skeleton.hp + 25
                print(' -- skeleton + 25 HP! --')
        ## -- Low health roll -- ## -- not working right, fix the >
            if skeleton.hp > 25:
                unluck1 = random.randrange(0,5)
                unluck2 = random.randrange(0,3)
                if unluck1 == unluck2:
                    damage = damage*4
                    print(' -- 4X Damage! -- ')
        ## -- Dodge -- ##
            unluck1 = random.randrange(0,7)
            unluck2 = random.randrange(0,7)
            if unluck1 == unluck2:
                damage = 0
                print(' -- Human Dodges Attack --')
            
        print('Skeleton attacks, does ' + str(damage) + ' damage!')
        Human.hp = Human.hp - damage
        print('Skeleton HP is: ', skeleton.hp, '\n')
        if Human.hp < 0:
            print(' !! Skeleton has killed the human! !! \n')


## -- Human ----------------------------------------------------##

class Person:
    def __init__(self, age, hp, attack_damage):
        self.age = age
        self.hp = hp
        self.attack_damage = attack_damage


    def walk(self):
        print("walking...")
    def run(self):
        print("running...")

    def attack(self):
    # -- damage component -- ##
        Human.hp = Human.hp 
        damage = Human.attack_damage
        #damage = random.randrange(15,25) + level

    ## -- crithit ranodm roll -- ##
        unluck1 = random.randrange(0,4)
        unluck2 = random.randrange(0,4)
        if unluck1 == unluck2:
            damage = damage*2
            print(' -- Double Damage! -- ')

    ## health up random roll ##
        unluck1 = random.randrange(0,5)
        unluck2 = random.randrange(0,8)
        if unluck1 == unluck2:
            Human.hp = Human.hp + 25
            print(' -- Humann + 25 HP! --')

    ## -- Skeleton attack dodge:
        unluck1 = random.randrange(0,7)
        unluck2 = random.randrange(0,7)
        if unluck1 == unluck2:
            damage = 0
            print(' -- Skeleton Dodges Attack --')


    ## HP Func
        print('- Attacking Skeleton -')
        skeleton.hp = skeleton.hp - damage
        print('Human attacks, does ' + str(damage) + ' damage!')
        print('Human HP is: ', Human.hp, '\n')
        if skeleton.hp < 0:
            print(' !! Human has killed the skeleton! !! \n')







## -- lifecheck - checks to see if either parties are alive -- ##
def lifecheck():
    if Human.hp <= 0:
        #print('You have died\n')
        print('Play again? y/n')
        nextlevel = input()
        if nextlevel == 'y':
            clear()
            mainlogic()
        elif nextlevel == 'n':
            clear()
            exit()
        else:
            print('Invalid option')
            #exit()
    if skeleton.hp <= 0:
        #print('You have killed the skeleton!\n')
        print('Play again? y/n')
        nextlevel = input()
        if nextlevel == 'y':
            clear()
            mainlogic()
        elif nextlevel == 'n':
            clear()
            exit()
        else:
            print('Invalid option')
            #exit()
        
    if skeleton.hp and Human.hp < 0:
        print('You both died')
    if skeleton.hp and Human.hp > 0:
        print('\nWhat would you like to do? a) Attack Monster b) Run From Monster\n')
    else:
        print('')






## -- Characters -- ##

#with open("levelmarker.tmp", "r") as file:  
    #level = file.read()



Human = Person(25, 130, random.randrange(10,25))

skeleton = Monster(10, 100, random.randrange(0,30))





mainlogic()

