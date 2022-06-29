from art import logo


# Add
def add(a, b):
    return a + b


# Subtract
def subtract(a, b):
    return a - b


# Multiply
def multiply(a, b):
    return a * b


# Divide
def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))

    end_of_calculation = False

    while not end_of_calculation:
        for operation in operations:
            print(operation)

        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What is the next number?: "))

        calc = operations[operation_symbol]
        answer = calc(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        check_end_of_calculations = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new "
                                          f"calculation. Type 'exit' to exit the program: ")

        if check_end_of_calculations == 'n':
            end_of_calculation = True
            calculator()
        elif check_end_of_calculations == 'exit':
            end_of_calculation = True
            print("Goodbye!")
        else:
            num1 = answer


calculator()
