import csv

def write_emp():
    f = open("School/emp_det.csv", "w", newline='')
    emps = []
    while True:
        number = int(input("Enter employee number : "))
        name = input("Enter employee name : ")
        address = input('Enter emplpoyee address : ')
        sal = int(input("Enter employee salary : "))

        emps.append([number, name, address, sal])
        ch = input("New Employee? [y/n] : ")
        if ch.lower() == "n":
            break
    w_obj = csv.writer(f)
    w_obj.writerows(emps)
    f.close()

def disp_emps():
    f = open("School/emp_det.csv", "r")
    r_obj = csv.reader(f)
    print("No.\t\tName\t\tAddress\t\tSalary")
    for i in r_obj:
        print(f"{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}")
    f.close()

def app_emp():
    f = open("School/emp_det.csv", "a", newline='')
    emps = []
    while True:
        number = int(input("Enter employee number : "))
        name = input("Enter employee name : ")
        address = input('Enter emplpoyee address : ')
        sal = int(input("Enter employee salary : "))

        emps.append([number, name, address, sal])
        ch = input("New Employee? [y/n] : ")
        if ch.lower() == "n":
            break
    a_obj = csv.writer(f)
    a_obj.writerows(emps)
    f.close()

def search_emp():
    f = open("School/emp_det.csv", "r")
    s_obj = csv.reader(f)
    num = input("Enter employee ID : ")
    for i in s_obj:
        if num == i[0]:
            print(f"\nEnployee ID : {i[0]}")
            print(f"Enployee Name : {i[1]}")
            print(f"Enployee Address : {i[2]}")
            print(f"Enployee Salary : {i[3]}\n")
        else:
            print("Employee Data does not exist")

while True:
    print("Employee Database")
    print("1. Create New Database \n2. Insert Employee Details \n3. Search Employee Details \n4. Display All Data \n5. EXIT")
    ch = int(input("Enter your choice : "))
    
    if ch == 1:
        write_emp()
    elif ch == 2:
        app_emp()
    elif ch == 3:
        search_emp()
    elif ch == 4:
        disp_emps()
    elif ch == 5:
        print("Exited Employee Database")
        break
    else:
        print("Wrong input, Please try another input")
        continue