# Taking input from the user
a = input("Enter the First Number: ")
b = input("Enter the Second number: ")
c = input("Enter the Operator (+, -, *, /, %): ")

# Converting input strings to integers
first = int(a)
second = int(b)

# Performing calculation based on the operator
if c == '+':
    print("Result:", first + second)
elif c == '-':
    print("Result:", first - second)
elif c == '*':
    print("Result:", first * second)
elif c == '/':
    if second != 0:
        print("Result:", first / second)
    else:
        print("Error: Division by zero!")
elif c == '%':
    if second != 0:
        print("Result:", first % second)
    else:
        print("Error: Modulo by zero!")
else:
    print("Invalid Operator")



print("Thank You For Giving Us time ")
print("And Thank You For using Calculator ")
