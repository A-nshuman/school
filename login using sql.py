import mysql.connector as con

cxn = con.connect(host = '', user = '', passwd = '', database = '')
cur = cxn.cursor()

uname = input("Enter username : ")
upwd = input("Enter password : ")

cur.execute(f"select uname, upwd from users where uname = '{uname}'")
user_data = cur.fetchone()

if user_data:
    if user_data[0] == uname and user_data[1] == upwd:
        print("Login Successful")
    else:
        print("Login Failed")
else:
    print("User does not exist")