"""
# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Jack Bauer")
"""

# Funciones con más de una entrada
def greet_with(a, b):
    print(f"Bienvenidos {a} de {b}")

name =input("Bienvenido Usuario\n    ¿Cual es su nombre?...\n ")
location =input("Donde se encuentra ubicado?\n ")

greet_with(name, location)

# Funciones con llaves de entrada, No altera la posición ya qué van unidas al argumento
def greet_with(a, b):
    print(f"Bienvenidos {a} de {b}")

name =input("Bienvenido Usuario\n    ¿Cual es su nombre?...\n ")
location =input("Donde se encuentra ubicado?\n ")

greet_with(b = name, a= location) # Los argumentos se vinculan al parametro
                                  # No importa si la entrada está en desorden
                                  # La función las letras según sus llaves asignadas