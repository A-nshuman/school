def traverse_list(numbers):
    stack = []
    for num in numbers:
        if num % 5 == 0:
            stack.append(num)
    return stack

def display_stack(stack):
    for num in stack:
        print(num, end=', ')

numbers = [2, 5, 10, 13, 20, 23, 45, 56, 60, 78]

result_stack = traverse_list(numbers)

print("Sample Output of the code should be:", end=' ')
display_stack(result_stack)
