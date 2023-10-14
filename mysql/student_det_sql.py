import mysql.connector as con
from prettytable import PrettyTable

cxn = con.connect(host = '', user = '', passwd = '', database = '')
cur = cxn.cursor()

def insertion():
    roll = int(input("Enter roll number : "))
    name = input("Enter name : ")
    stream = input("Enter stream : ")
    marks = float(input("Enter marks : "))
    grade = input("Enter grade : ")
    clas = int(input("Enter class : "))

    cur.execute("insert into stud(RollNo, name, stream, avg_marks, grade, class) values({},'{}','{}',{},'{}',{})".format(roll, name, stream, marks, grade, clas))
    cxn.commit()
    print('Data inserted successfully!')

def deletion():
    roll = input("Enter roll number to delete : ")
    cur.execute(f"delete from stud where RollNo = {roll}")
    print("Record deleted from table")

def updation():
    roll = input("Type roll number of student to be updated : ")
    name = input("Enter name : ")
    stream = input("Enter stream : ")
    marks = float(input("Enter marks : "))
    grade = input("Enter grade : ")
    clas = int(input("Enter class : "))

    query = f"update stud set name = '{name}', stream = '{stream}', avg_marks = {marks}, grade = '{grade}', class = {clas} where RollNo = {roll}"
    cur.execute(query)
    print("Record successfully updated")

def display():
    cur.execute("select * from stud")
    user_data = cur.fetchall()

    tab = PrettyTable(["RollNo", "Name", "Stream", "Marks", "Grade", "Class"])
    for i in user_data:
        tab.add_row([f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[3]}", f"{i[4]}", f"{i[5]}"])

    print(tab)

while True:
    print("Student Details")
    print("1. INSERT \n2. DELETE \n3. UPDATE\n4. DISPLAY\n5. EXIT \n")

    ch = int(input("Enter your choise : "))

    if ch == 1: insertion()
    elif ch == 2: deletion()
    elif ch == 3: updation()
    elif ch == 4: display()
    else: break
