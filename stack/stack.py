def create():
    global stack
    stack = []
    print("An empty stack has been created")
     
def push(stack):
    ele = input("Enter element to be pushed : ")
    stack.append(ele)
     
def pop(stack):
    poped = stack.pop()
    print(f"Poped element is {poped}")

def peek(stack):
    print(f"The top element is {stack[-1]}")

def display(stack):
    print("The stack is", stack)

def isEmpty(stack):
    if stack == []:
        print("Stack is empty")
    else:
        print("Stack is not empty")

while True:
    print("\nData Structure Menu")
    print("1. Create Stack \n2. Push \n3. Pop \n4. Peek \n5. Display \n6. Is Empty \n7. EXIT")
    ch = int(input("Enter your choice : "))

    if ch == 1:
        create()

    elif ch == 2:
        try:
            push(stack)
        except Exception:
            print("Create a stack first")

    elif ch == 3:
        try:
            pop(stack)
        except Exception:
            print("Create a stack first")

    elif ch == 4:
        try:
            peek(stack)
        except Exception:
            print("Create a stack first")

    elif ch == 5:
        try:
            display(stack)
        except Exception:
            print("Create a stack first")

    elif ch == 6:
        try:
            isEmpty(stack)
        except Exception:
            print("Create a stack first")

    elif ch == 7:
        print("Program exited successfully")
        break