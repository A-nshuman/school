CStack = []

def AddCustomer(Customer, CStack):
    CStack.append(Customer)
    print("Customer information added successfully.")

def DeleteCustomer(CStack):
    if len(CStack) > 0:
        deleted_customer = CStack.pop()
        print("Deleted Customer:", deleted_customer)
    else:
        print("Stack is empty. No customer to delete.")

while True:
    print("1. Add Customer \n2. Delete Customer \n3.EXIT")
    ch = int(input("Enter your choice : "))

    if ch == 1:
        new_customer = input("Enter customer name : ")
        AddCustomer(new_customer, CStack)
        print("Customer information in the stack:", CStack)

    elif ch == 2:
        DeleteCustomer(CStack)
        print("Customer information in the stack:", CStack)
        
    elif ch == 3:
        print("Program Exited Successfully")
        break

    else:
        print("Enter a valid choice")
        continue
