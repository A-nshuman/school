import random
from time import sleep

def roll_dice():
    print("Dice Rolling", end='')
    sleep(0.5)
    print(".", end='')
    sleep(0.5)
    print(".", end='')
    sleep(0.5)
    print(".")
    sleep(1)
    num = random.randint(1,6)
    print(f"You got {num}")

while True:
    print("1. Roll Dice\n2. Exit")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        roll_dice()

    elif choice == 2:
        print("GoodNight ( ͡~ ͜ʖ ͡° )")
        break

    else:
        print("Wrong Choice, Try Again")
        continue
