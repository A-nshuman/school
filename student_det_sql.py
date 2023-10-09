import mysql.connector as con

cxn = con.connect(host = 'localhost', user = 'root', passwd = '123456789', database = 'school')
cur = cxn.cursor()

while True:
    qn = input("Do you want to add a record ? [y/n] : ")
    
    if qn.lower() == 'y':
        roll = int(input("Enter roll number : "))
        name = input("Enter name : ")
        stream = input("Enter stream : ")
        marks = float(input("Enter marks : "))
        clas = int(input("Enter class : "))
        grade = input("Enter grade : ")

        cur.execute("insert into stud(RollNo, name, stream, avg_marks, grade, class) values({},'{}','{}',{},'{}',{})".format(roll, name, stream, marks, grade, clas))
        cxn.commit()
        print('Data inserted successfully!')
    
    else:
        break