import random
from time import sleep

def roll_dice():
    print("Dice Rolling", end='')
    for i in range(1,4):
        sleep(0.5)
        print(".", end="")
    sleep(0.5)
    num = random.randint(1,6)
    print(f"\nYou got {num}")

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
