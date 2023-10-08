import pickle

def add_player():
    number = int(input("Enter player number: "))
    name = input("Enter player name: ")
    age = int(input("Enter player age: "))
    player = {'number': number, 'name': name, 'age': age}
    with open('player.dat', 'ab') as file:
        pickle.dump(player, file)
    print("Player added successfully!")

def remove_player():
    number = int(input("Enter player number to remove: "))
    players = []
    with open('player.dat', 'rb') as file:
        while True:
            try:
                player = pickle.load(file)
                if player['number'] != number:
                    players.append(player)
            except EOFError:
                break
    with open('player.dat', 'wb') as file:
        for player in players:
            pickle.dump(player, file)
    print("Player removed successfully!")

def display_all_data():
    with open('player.dat', 'rb') as file:
        while True:
            try:
                player = pickle.load(file)
                print("Player Number:", player['number'])
                print("Player Name:", player['name'])
                print("Player Age:", player['age'])
                print()
            except EOFError:
                break

def search_player():
    number = int(input("Enter player number to search: "))
    with open('player.dat', 'rb') as file:
        while True:
            try:
                player = pickle.load(file)
                if player['number'] == number:
                    print("Player Name:", player['name'])
                    print("Player Age:", player['age'])
                    return
            except EOFError:
                break
    print("Player not found!")

while True:
    print("1. Add player")
    print("2. Remove player")
    print("3. Display all data")
    print("4. Search player")
    print("5. Quit")
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        add_player()
    elif choice == 2:
        remove_player()
    elif choice == 3:
        display_all_data()
    elif choice == 4:
        search_player()
    elif choice == 5:
        break
    else:
        print("Invalid choice! Please try again.")





# import pickle

# class Player:
#     def __init__(self, number, name, age):
#         self.number = number
#         self.name = name
#         self.age = age

# def write_player_details():
#     try:
#         with open("player_details.bin", "ab") as file:
#             number = int(input("Enter player number: "))
#             name = input("Enter player name: ")
#             age = int(input("Enter player age: "))
#             player = Player(number, name, age)
#             pickle.dump(player, file)
#             print("Player details added successfully!")
#     except:
#         print("An error occurred while writing player details.")

# def delete_player_details():
#     try:
#         number = int(input("Enter player number to delete: "))
#         with open("player_details.bin", "rb") as file1, open("temp.bin", "wb") as file2:
#             while True:
#                 try:
#                     player = pickle.load(file1)
#                     if player.number != number:
#                         pickle.dump(player, file2)
#                 except EOFError:
#                     break
#         import os
#         os.remove("player_details.bin")
#         os.rename("temp.bin", "player_details.bin")
#         print("Player details deleted successfully!")
#     except:
#         print("An error occurred while deleting player details.")

# def display_all_player_details():
#     try:
#         with open("player_details.bin", "rb") as file:
#             while True:
#                 try:
#                     player = pickle.load(file)
#                     print("Player Number:", player.number)
#                     print("Player Name:", player.name)
#                     print("Player Age:", player.age)
#                     print("-" * 30)
#                 except EOFError:
#                     break
#     except:
#         print("An error occurred while displaying player details.")

# def search_player_details():
#     try:
#         number = int(input("Enter player number to search: "))
#         with open("player_details.bin", "rb") as file:
#             while True:
#                 try:
#                     player = pickle.load(file)
#                     if player.number == number:
#                         print("Player Number:", player.number)
#                         print("Player Name:", player.name)
#                         print("Player Age:", player.age)
#                         print("-" * 30)
#                         break
#                 except EOFError:
#                     print("Player details not found.")
#                     break
#     except:
#         print("An error occurred while searching player details.")

# while True:
#     print("1. Append player details")
#     print("2. Delete player details")
#     print("3. Display all player details")
#     print("4. Search player details")
#     print("5. Exit")
#     choice = input("Enter your choice (1-5): ")
#     if choice == "1":
#         write_player_details()
#     elif choice == "2":
#         delete_player_details()
#     elif choice == "3":
#         display_all_player_details()
#     elif choice == "4":
#         search_player_details()
#     elif choice == "5":
#         print("Exiting program...")
#         break
#     else:
#         print("Invalid choice! Please enter a valid choice.")







# import pickle
# from prettytable import PrettyTable

# def write_pl():
#     f = open("School/player.dat", "wb")
#     pl = []
#     while True:
#         num = int(input("Enter player number : "))
#         name = input("Enter player name : ")
#         age = int(input("Enter player age : "))

#         pl.append([num, name, age])
#         pickle.dump(pl, f)
#         ch = input("New Player? [y/n] : ")
#         if ch.lower() == "n":
#             break
#     f.close()

# def disp_pl():
#     f = open("School/player.dat", "rb")
#     tab = PrettyTable(['Number', 'Name', 'Age'])
#     for i in pickle.load(f):
#         tab.add_row([f'{i[0]}', f'{i[1]}', f'{i[2]}'])
#     print(tab)

# while True:
#     print('1. New Database \n2. Insert \n3. Delete \n4. Display \n5. EXIT')
#     ch = int(input("Enter your choice : "))

#     if ch == 1:
#         write_pl()
#     elif ch == 4:
#         disp_pl()
#     elif ch == 5:
#         break