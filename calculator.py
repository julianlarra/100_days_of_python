#  add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the first number?: "))

    for simbol in operations:
        print(simbol)
    should_continue = True

    while should_continue:

        operation_simbol = input("Pick an operation:\n")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_simbol]

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_simbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating whit {answer}, or type 'n' to estar a new calculation.:") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()


