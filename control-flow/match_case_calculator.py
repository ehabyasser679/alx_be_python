num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

Operation = input("Choose the operation (+, -, *, /): ")
match Operation:
    case "+":
        Result = num1 + num2
    case "-":
        Result = num1 - num2
    case "*":
        Result = num1 * num2
    case "/":
        if num2 == 0 and Operation == "/":
            print("Cannot divide by zero.")
        else:
            Result = num1 / num2
    case _:
        print("Invalid input.")
        
print("The result is", Result)
