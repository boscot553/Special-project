import random
import time
crate = input("Pick a crate(basic, battle, daily, subscription) ")
if crate == "basic":
    x = random.randint(0, 20)
    y = random.randint(1, 15)
    if x <= 15:
        print("Bronze")
        print(y)
    elif x == 16 or x == 17 or x == 18:
        print("Iron")
        print(y)
    elif x == 19:
        print("Gold")
        print(y)
    else:
        print("Upgrade to battle")
        crate = "battle"
    
if crate == "battle":
    chances = random.randint(3, 5)
    print(f"{chances} cards")
    time.sleep(3)
    for i in range(chances):
        x = random.randint(0, 100)
        y = random.randint(1, 15)
        if x <= 35:
            print("Bronze")
        elif x > 35 and x <= 65:
            print("Iron")
        elif x > 65 and x <= 80:
            print("Gold")
        elif x > 80 and x <= 90:
            print("Platnium")
        elif x > 90 and x <= 97:
            print("Diamond")
        else:
            print("Emerald")
        print(y)

if crate == "daily":
    for i in range(3):
        x = random.randint(0, 200)
        y = random.randint(1, 15)
        if x <= 50:
            print("Bronze")
        elif x > 50 and x <= 100:
            print("Iron")
        elif x > 100 and x <= 150:
            print("Gold")
        elif x > 150 and x <= 175:
            print("Platnium")
        elif x > 175 and x <= 190:
            print("Diamond")
        elif x > 190 and x <= 195:
            print("Emerald")
        else:
            print("Wild")
        print(y)

if crate == "subscription":
    for i in range(3):
        y = random.randint(1, 15)
        print(f"Bronze: {y}")
    for i in range(2):
        y = random.randint(1, 15)
        print(f"Iron: {y}")
    for i in range(2):
        y = random.randint(1, 15)
        print(f"Gold: {y}")
    for i in range(2):
        y = random.randint(1, 15)
        print(f"Platnium: {y}")
    for i in range(1):
        y = random.randint(1, 15)
        print(f"Diamond: {y}")