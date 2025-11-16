import threading
import keyboard
import time
import random
elixir = 0
game =''
main = []
deck = ["skeleton", "goblin", "log", "knight", "Armoured gaurd", "Wizard", "Fireball", "Bomber"]
randomizer = 0

def elixir_count():
    while game != "over":
        time.sleep(2)
        elixir += 1

def select_card():
    for i in range(4):
        randomizer = random.randint(1, 8)
        if randomizer == 1:
            main.append(deck[0])
        if randomizer == 2:
            main.append(deck[1])
        if randomizer == 3:
            main.append(deck[2])
        if randomizer == 4:
            main.append(deck[3])
        if randomizer == 5:
            main.append(deck[4])
        if randomizer == 6:
            main.append(deck[5])
        if randomizer == 7:
            main.append(deck[6])
        if randomizer == 8:
            main.append(deck[7])
    print(main)

select_card()

def picking():
    while game != 'over':
        deck_number = random.randint(0, 7)
        while deck[deck_number] in main:
            deck_number = random.randint(0, 7)
        if deck_number == 0:
            main.append(deck[0])
        if deck_number == 1:
            main.append(deck[1])
        if deck_number == 2:
            main.append(deck[2])
        if deck_number == 3:
            main.append(deck[3])
        if deck_number == 4:
            main.append(deck[4])
        if deck_number == 5:
            main.append(deck[5])
        if deck_number == 6:
            main.append(deck[6])
        if deck_number == 7:
            main.append(deck[7])
        removing = input(">  ")
        if removing == "1":
            main.remove(main[0])
            print(main)
        elif removing == "2":
            main.remove(main[1])
            print(main)
        elif removing == "3":
            main.remove(main[2])
            print(main)
        elif removing == "4":
            main.remove(main[3])
            print(main)
       
    


picking()

