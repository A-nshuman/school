import functions as fun

while True:
    print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
    choice = int(input("Enter your choice : "))
    if choice == 5:
        print("Menu Exited")
        break

    else:
        a = float(input("Enter first number : "))
        b = float(input("Enter second number : "))
    
        if choice == 1:
            fun.add(a,b)

        elif choice == 2:
            fun.sub(a,b)

        elif choice == 3:
            fun.mul(a,b)

        elif choice == 4:
            fun.div(a,b)