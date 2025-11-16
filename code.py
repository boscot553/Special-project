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