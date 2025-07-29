import art
print(art.logo)

# Creamos las funciones para cada operación
def add(n1, n2):
    """Suma"""
    return n1 + n2

def subtract(n1, n2):
    """Resta"""
    return n1 - n2

def multiply(n1, n2):
    """Multiplica"""
    return n1 * n2

def divide(n1, n2):
    """Divide"""
    return n1 / n2

# Creamos un diccionario para almacenar las funciones
# Asignamos a los pares clave valor las funciones sin () para no activarlas
operations = {"+":add, "-":subtract, "*":multiply, "/":divide}

num1 = float(input("What's the first number?: "))
result = 0
start = True
while start:

    print("+\n-\n*\n/")
    operation = str(input("Pick an operation: "))
    num2 = float(input("What's next number?: "))

    if operation == "+":
        result_add = operations["+"](num1,num2)
        result += result_add
        print(f"{num1} + {num2} = {result}")

    if operation == "-":
        result_subtract = operations["-"](num1, num2)
        result += result_subtract
        print(f"{num1} - {num2} = {result}")

    if operation == "*":
        result_multiply = operations["*"](num1, num2)
        result += result_multiply
        print(f"{num1} * {num2} = {result}")

    if operation == "/":
        result_divide = operations["/"](num1, num2)
        result += result_divide
        print(f"{num1} / {num2} = {result}")

    yes_or_no = input(f"Type 'y' to continue whit {result}, or type 'n' to start a new calculation: ").lower()
    if yes_or_no == "y":
        num1 = result
        result = 0
    if yes_or_no == 'n':
        result = 0
        print("\n" *12)
    else:
        print("Select a correct option")