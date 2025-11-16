num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

Operation = input("Choose the operation (+, -, *, /): ")

if Operation == "+":
    Result = num1 + num2
elif Operation == "-":
    Result = num1 - num2
elif Operation == "*":
    Result = num1 * num2
elif Operation == "/":
    Result = num1 / num2
elif num2 == 0:
    print("Cannot divide by zero")

print("The result is", Result)