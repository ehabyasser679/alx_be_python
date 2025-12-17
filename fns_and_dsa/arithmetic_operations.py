from operator import add, sub, mul, truediv
OPERATIONS = {
    "add": add,
    "subtract": sub,
    "multiply": mul,
    "divide": truediv
}
def perform_operation(num1: float, num2: float, operation: str):
    if operation not in OPERATIONS:
        raise ValueError(f"Invalid operation: {operation}")
    if operation == "divide" and num2 == 0:
        raise ZeroDivisionError("Cannor divide by zero")
    return OPERATIONS[operation](num1, num2)
