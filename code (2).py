import threading
import time
import random
game =''
main = []
deck =[ {
    "name": "Bomber",
    "elixir": 2},
    {
    "name": "Rider",
    "elixir": 3},
    {
    "name": "Skeleton",
    "elixir": 2},
    {
    "name": "Goblin gankers",
    "elixir": 3},
    {
    "name": "The log",
    "elixir": 2},
    {
    "name": "Mecha",
    "elixir": 5},
    {
    "name": "Archers",
    "elixir": 3},
    {
    "name": "Wizard",
    "elixir": 2},
]

class mana():
    def __init__ (self, elixir):
        self.elixir = elixir

mana(0)

randomizer = 0

def elixir_count():
    while game != "over":
        time.sleep(2)
        mana.elixir += 1
        print(mana.elixir)

def select_card():
    x = 0
    while x != 4:
        randomizer = random.randint(1, 8)
        if randomizer == 1:
            if deck[0]["name"] not in main:
                main.append(deck[0]["name"])
                x += 1
        if randomizer == 2:
            if deck[1]["name"] not in main:
                main.append(deck[1]["name"])
                x += 1
        if randomizer == 3:
            if deck[2]["name"] not in main:
                main.append(deck[2]["name"])
                x += 1
        if randomizer == 4:
            if deck[3]["name"] not in main:
                main.append(deck[3]["name"])
                x += 1
        if randomizer == 5:
            if deck[4]["name"] not in main:
                main.append(deck[4]["name"])
                x += 1
        if randomizer == 6:
            if deck[5]["name"] not in main:
                main.append(deck[5]["name"])
                x += 1
        if randomizer == 7:
            if deck[6]["name"] not in main:
                main.append(deck[6]["name"])
                x += 1
        if randomizer == 8:
            if deck[7]["name"] not in main:
                main.append(deck[7]["name"])
                x += 1
    print(main)

select_card()

def picking():
    while game != 'over':
        deck_number = random.randint(0, 7)
        while deck[deck_number]["name"] in main:
            deck_number = random.randint(0, 7)
        if deck_number == 0:
            main.append(deck[0]["name"])
        if deck_number == 1:
            main.append(deck[1]["name"])
        if deck_number == 2:
            main.append(deck[2]["name"])
        if deck_number == 3:
            main.append(deck[3]["name"])
        if deck_number == 4:
            main.append(deck[4]["name"])
        if deck_number == 5:
            main.append(deck[5]["name"])
        if deck_number == 6:
            main.append(deck[6]["name"])
        if deck_number == 7:
            main.append(deck[7]["name"])
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

thread_elixir_count = threading.Thread(target=elixir_count)
thread_elixir_count.start()
picking()


       
    

