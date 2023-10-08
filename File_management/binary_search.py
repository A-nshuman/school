import pickle

def write_info():
    f = open('School/Stud_det.dat', 'wb')
    stud = []
    while True:
        roll = int(input("Enter roll number : "))
        name = input("Enter student name : ")
        stud.append([roll, name])
        pickle.dump(stud, f)

        ch = input("New student? [y/n] : ")
        if ch.lower() == "n":
            break

    f.close()

def search():
    f = open('School/Stud_det.dat', 'rb')
    roll = int(input("Enter student roll number : "))
    lo = pickle.load(f)
    for i in lo:
        if roll == i[0]:
            # print(f"Student roll number : {i[0]}")
            print(f"Student name : {i[1]}")
        else:
            print("Student not registered in record")
            q = input("Do you want to regiester student in record ? [y/n] : ")
            if q.lower() == "y":
                write_info()
            else:
                break
    f.close()

while True:
    print("1. Write Data \n2. Search Data \n3. EXIT")
    ch = int(input("Enter your choice : "))

    if ch == 1:
        write_info()
    elif ch == 2:
        search()
    elif  ch == 3:
        break
    else:
        print("Wrong choice, Pls try another input.")
        continue