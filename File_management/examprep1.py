# def Create():
#     global stack
#     stack = input("Enter stack name : ")
#     stack = []
#     print("Stack Created\n")

# def Push(stack):
#     inp = input("Enter item : ")
#     stack.append(inp)
#     print(f"{inp} added to stack\n")
    
# def Pop(stack):
#     x = stack.pop()
#     print(f"Item poped : {x}\n")

# def Peek(stack):
#     print(f"Top most item = {stack[-1]}\n")

# def Display(stack):
#     for i in stack:
#         print(i)
#     print("\n")

# def isEmpty(stack):
#     if stack == []:
#         print("Stack is empty")
#     else:
#         print("Stack is not empty")

# while True:
#     print("1.Create \n2.Push \n3.Pop \n4.Peek \n5.Display \n6.EXIT")
#     ch = int(input("Enter your choice : "))

#     if ch == 1:
#         Create()

#     elif ch == 2:
#         try:
#             Push(stack)
#         except Exception:
#             print("Create a stack")
    
#     elif ch == 3:
#         try:
#             Pop(stack)
#         except Exception:
#             print("Create a stack")
    
#     elif ch == 4:
#         try:
#             Peek(stack)
#         except Exception:
#             print("Create a stack")

#     elif ch == 5:
#         try:
#             Display(stack)
#         except Exception:
#             print("Create a stack")

#     else:
#         break

# ------------------------------------------------------------

# def cube(x):
#     print(f"Cube of {x} is {x**3}")

# num = int(input("Enter a number : "))
# cube(num)

# ------------------------------------------------------------

# summ = 0
# while True:
#     num = input("Enter a number : ")
#     if num.lower() == "done":
#         break
#     else:
#         summ += int(num)

# print(summ)

# ------------------------------------------------------------

#Write a Python program to print only the positive Numbers from the given List.

# list1 = [11, -21, 0, 45, 66, -93]
# for i in list1:
#     if i >= 0:
#         print(i)

# ------------------------------------------------------------

# Python Program to Calculate Profit or Loss by using elif Statement. It should produce the following output.

# i = 1
# while i<=3:
#     actual = int(input("Enter Actual Amount : "))
#     sales = int(input("Enter Sales Amount : "))
#     if sales > actual:
#         print(f"Total Loss : {sales-actual}")
#     elif sales < actual:
#         print(f"Total Profit : {actual-sales}")
#     else:
#         print("No Profit No Loss")
#     i+=1

# ------------------------------------------------------------

# def numberTeller():
#     while True:
#         num = int(input("Enter a number in range 0 to 999 : "))
#         if num in range(0,1000):
#             if len(str(num)) == 1:
#                 print("It is 1 digit number")
#             elif len(str(num)) == 2:
#                 print("It is 2 digit number")
#             elif len(str(num)) == 3:
#                 print("It is 3 digit number")
#             break
#         else:
#             print("Enter a number in range 0 to 999")
#             continue
# numberTeller()

# ------------------------------------------------------------

# def divCheck(num):
#     if num >= 0:
#         if num % 5 == 0:
#             print("number is divisible by 5")
#         elif num % 11 == 0:
#             print("number is divisible by 11")
#         elif num % 5 == 0 and num % 11 == 0:
#             print("number is divisible by 5 and 11")
#         else:
#             print("Number is neither")

# num = int(input("Enter a number : "))
# divCheck(num)

# ------------------------------------------------------------

# def My_Text():
#     with open("School/My_Text_File.txt", "w") as f:
#         S1="I love India All Indians are my brother and sisters india is My country"
#         f.write(S1)
#         f.close()
    
#     with open("School/My_Text_File.txt", "r") as f:
#         data = f.readline()
#         print(data)
#         f.close()
# My_Text()

# ------------------------------------------------------------

# def My_Text():
#     count = 0
#     with open("School/My_Text_File.txt", "r") as f:
#         data = f.read()
#         new = data.split()
#         for i in new:
#             if i == "India" or i == "india":
#                 print(i)
#                 count += 1
#             else:
#                 pass
#         print(f"Number = {count}")

# My_Text()

# ------------------------------------------------------------
# import pickle

# def create():
#     lis = []
#     with open("School/Book_Details.dat", "wb") as f:
#         x = 1
#         while x <= 3:
#             num = int(input("Enter book number: "))
#             name = input("Enter book name: ")
#             aut = input("Enter author name: ")
#             price = input("Enter book price: ")
#             lis.append([num, name, aut, price])
#             x += 1
#         pickle.dump(lis, f)
#     f.close()

# def CountRec(aut):
#     count = 0
#     with open("School/Book_Details.dat", "rb") as file:
#         data = pickle.load(file)
#         for i in range(len(data)):
#             if aut == data[i][2]:
#                 count += 1
#         print(f"Number of books: {count}")

# author = input("Enter author name: ")
# CountRec(author)

# ------------------------------------------------------------

# import pickle

# def storage():
#     with open("School/STUDENT_INFO.DAT", "wb") as f:
#         lis = []
#         i = 1
#         ch = int(input("How many records : "))
#         while i <= ch:
#             num = int(input("Enter admission number : "))
#             name = input("Enter name : ")
#             per = float(input("Enter percentage : "))
#             lis.append((num, name, per))
#             i+=1
#         pickle.dump(lis, f)
#     f.close()

# def COUNTREC():
#     with open("School/STUDENT_INFO.DAT", "rb") as f:
#         data = pickle.load(f)
#         for i in data:
#             if i[2] >= 60:
#                 print(i)
#         f.close()

# storage()
# COUNTREC()

# ------------------------------------------------------------

# a={1:"A",2:"B",3:"C"} 
# print(a.setdefault(3))

# ------------------------------------------------------------

# def read_vow():
#     count = 0
#     f = open("School/My_Text_File.txt", "r")
#     while True:
#         line = f.readline()
#         if line == '':
#             break
#         else:
#             for i in line:
#                 if i.lower() in "aeiou":
#                     count+=1
#     f.close()
# read_vow()

# def read_vow():
#     with open("School/poem.txt", "r") as f:
#         lines = f.readlines()
#         for i in lines:
#             count = 0
#             for char in i:
#                 if char.lower() in "aeiou":
#                     count += 1
#             print(f"Number of vowels in the line = {count}")
#     f.close()
# read_vow()

# ------------------------------------------------------------

# def smallLarge(lis):
#     largest = lis[0]
#     smallest = lis[0]
#     for i in lis:
#         if i > largest:
#             largest = i
#         if i < smallest:
#             smallest = i

#     print(f"Largest = {largest}")
#     print(f"Smallest = {smallest}")

# lis = [1,2,4,453,234,432,34,1000]
# smallLarge(lis)

# ------------------------------------------------------------

# def Display(str): 
#     m="" 
#     for i in range(0,len(str)): 
#         if(str[i].isupper()): 
#             m=m+str[i].lower() 
#         elif str[i].islower(): 
#             m=m+str[i].upper() 
#         else: 
#             if i%2==0: 
#                 m=m+str[i-1] 
#             else: 
#                 m=m+"#" 
#                 print(m) 
# Display('Fun@Python3.0') 

# ------------------------------------------------------------

# lst1 = [10, 15, 20, 25, 30] 
# lst1.insert( 3, 4) 
# lst1.insert( 2, 3) 
# print(lst1)
# print (lst1[-5]) 

# x = [[10.0, 11.0, 12.0],[13.0, 14.0, 15.0]] 
# y = x[1][2] 
# print(y) 

# T=(100) 
# print(T*2) 

# ------------------------------------------------------------

# def ask():
#     num = int(input("Hpw mnua recoeds? : "))
#     global dic
#     dic = {}
#     for i in range(num):
#         name = input("Enter name : ")
#         sal = int(input("Enter salary : "))
#         dic[name] = sal

# ask()
# print(dic)

# ------------------------------------------------------------

# def my_func(var1=100, var2=200): 
#     var1+=10 
#     var2 = var2 - 10 
#     return var1+var2 
# print(my_func(50),my_func()) 

# ------------------------------------------------------------

# Write and execute a function-based menu driven python program to store the 
# employee details (empno, name, and dept) into a binary file employee.dat 
# and search for a particular employee based on the employee number entered 
# by the user.

# import pickle
# def enter():
#     with open("School/employe.dat", "wb") as f:
#         lis = []
#         ch = int(input("How many : "))
#         for i in range(ch):
#             num = int(input("Enter number : "))
#             name = input("Enter name : ")
#             dept = int(input("Enter dept : "))
#             lis.append([num, name, dept])
#             pickle.dump(lis, f)
#     f.close()

# def search():
#     with open("School/employe.dat", "rb") as f:
#         inp = int(input("Enter number : "))
#         data = pickle.load(f)
#         for i in data:
#             if i[0] == inp:
#                 print(i)
#     f.close()

# enter()
# search()

# ------------------------------------------------------------

# Write and execute a function-based menu driven python program to store the 
# student details (adno, name, and class) into a CSV file students.csv and 
# perform read operation.

# import csv

# def enter():
#     with open("School/sinfo.csv", "w", newline='') as f:
#         lis = []
#         n = int(input("hoe manu : "))
#         for i in range(n):
#             num = int(input("Enter number : "))
#             name = input("Enter name : ")
#             clas = int(input("Enter class : "))
#             lis.append([num, name, clas])
#         w = csv.writer(f)
#         w.writerows(lis)
#     f.close()

# def read():
#     with open("School/sinfo.csv", "r") as f:
#         r = csv.reader(f)
#         for i in r:
#             print(i)

# enter()
# read()

# ------------------------------------------------------------

# def know(st):
#     up = 0
#     down = 0
#     for i in st:
#         if i.isupper():
#             up+=1
#         elif i.islower():
#             down+=1
#     print("Upper = ", up)
#     print("Lower = ", down)

# st = input("Enter a string : ")
# know(st)

# ------------------------------------------------------------

# Write a function in Python that counts the number of “Me” or “My” words 
# present in a text file “STORY.TXT”. If the “STORY.TXT” contents are as 
# follows: 
# My first book was Me and My Family. It gave me chance to be Known to the 
# world. 
# The output of the function should be: 
# Count of Me/My in file: 4 

# def count():
#     with open("School/story.txt", "r") as f:
#         c = 0
#         data = f.read()
#         sl = data.split()
#         for i in sl:
#             if i.lower() == 'me' or i.lower() == 'my':
#                 c+=1
#         print(f"Number of me/my = {c}")
# count()

# ------------------------------------------------------------

# X = 10
# def Global(Y):
#     global X
#     X = 15
#     X+=Y
#     return(X+Y)

# K = Global(X)
# print(X+K)

# X = 10, X = 15, Global(X) = 15+10 = 25
# K = Global(X), X = 25, X = 10, K = 10+25 = 35
# K+X = 60

# ------------------------------------------------------------
# Write a function in Python POP_ME(Num_List), where Num_List is a stack 
# implemented by a list of numbers. The function should returns the value deleted from 
# the stack.

# def POP_ME(Num_List):
#     poped = Num_List.pop()
#     return poped

# L = [1,23,4,55,2,123]
# print(POP_ME(L))

# ------------------------------------------------------------

# Write a user defined function in Python PUSH_ME(Num_List), where Num_List is a 
# list of numbers. From this list push all numbers divisible by 2 into a stack 
# implemented by using a list. Display the stack if it has at least one element, otherwise 
# display appropriate error message

# def PUSH_ME(Num_List):
#     stack = []
#     for i in Num_List:
#         if i % 2 == 0:
#             stack.append(i)
#     return stack

# L = [1,23,4,55,2,123]
# print(PUSH_ME(L))

# ------------------------------------------------------------

# Write a function in Python that counts the number of “India” or “india” words present 
# in a text file “My_Text_File.txt”.
# If the My_Text_File.txt” contents are as follows:
# S1="I love India All Indians are my brother and sisters india is My country"

# def teller():
#     with open("School/My_Text_File.txt", "r") as f:
#         data = f.read()
#         x = data.split()
#         count = 0
#         for i in x:
#             if i.lower() == "india":
#                 count+=1
#                 print(i)
#         print("Number of India/india =", count)
#     f.close()
# teller()