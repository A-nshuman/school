import csv
from prettytable import PrettyTable

def write_cus():
    f = open("School/cus_det.csv", "w", newline='')
    emps = []
    while True:
        s_no = int(input("Enter customer ID : "))
        date = input("Enter date [dd/mm/yyy] : ")
        name = input("Enter customer name : ")
        address = input('Enter customer address : ')
        bill = int(input("Enter customer bill : "))

        emps.append([s_no, date, name, address, bill])
        ch = input("New Customer? [y/n] : ")
        if ch.lower() == "n":
            break
    w_obj = csv.writer(f)
    w_obj.writerows(emps)
    f.close()

def disp_cus():
    f = open("School/cus_det.csv", "r")
    r_obj = csv.reader(f)
    tab = PrettyTable(["ID", "Date", "Name", "Address", "Bill"])
    for i in r_obj:
        tab.add_row([f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[3]}", f"{i[4]}"])
    print(tab)
    f.close()

def add_cus():
    f = open("School/cus_det.csv", "a", newline='')
    emps = []
    while True:
        s_no = int(input("Enter customer ID : "))
        date = input("Enter date [dd/mm/yyy] : ")
        name = input("Enter customer name : ")
        address = input('Enter customer address : ')
        bill = int(input("Enter customer bill : "))

        emps.append([s_no, date, name, address, bill])
        ch = input("New Customer? [y/n] : ")
        if ch.lower() == "n":
            break
    w_obj = csv.writer(f)
    w_obj.writerows(emps)
    f.close()

def search_cus():
    f = open("School/cus_det.csv", "r")
    s_obj = csv.reader(f)
    num = input("Enter customer ID : ")
    for i in s_obj:
        if num == i[0]:
            print(f"\nCustomer ID : {i[0]}")
            print(f"Date of shopping : {i[1]}")
            print(f"Customer Name : {i[2]}")
            print(f"Customer Address : {i[3]}")
            print(f"Customer Bill : {i[4]}\n")
        else:
            print("Customer Data does not exist")

def del_cus():
    ID = int(input("Enter customer ID : "))
    with open("School/cus_det.csv", "r") as file:
        r_obj = csv.reader(file)
        nlis = list(r_obj)
        for i in nlis:
            if int(i[0]) == ID:
                global ind
                ind = nlis.index(i)
        del nlis[ind]

    with open("School/cus_det.csv", "w", newline='') as file:
        w_obj = csv.writer(file)
        w_obj.writerows(nlis)

while True:
    print("Customer Database")
    print("1. Create New Database \n2. Insert Customer Details \n3. Search Customer Details \n4. Display All Data \n5. Delete Customer Details \n6. EXIT")
    ch = int(input("Enter your choice : "))
    
    if ch == 1:
        write_cus()
    elif ch == 2:
        add_cus()
    elif ch == 3:
        search_cus()
    elif ch == 4:
        disp_cus()
    elif ch == 5:
        del_cus()
    elif ch == 6:
        print("Exited Customer Database")
        break
    else:
        print("Wrong input, Please try another input")
        continue
