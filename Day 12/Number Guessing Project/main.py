from art import logo
import random

print(logo)

def easy():
    global NUMBER
    global LIVES
    LIVES = 10

    while LIVES > 0:
        print(f"\nYou have {LIVES} attempts remaining to guess the number.")
        choice = int(input("Make a guess: "))

        if choice < NUMBER:
            LIVES -= 1
            print("Too Low")

        if choice > NUMBER:
            LIVES -= 1
            print("Too High")

        if choice == NUMBER:
            print(f"You got it! The answer was: {choice}")
            print("\nThanks for playing")
            LIVES = 0



def hard():
    global NUMBER
    global LIVES
    LIVES = 5

    while LIVES > 0:
        print(f"\nYou have {LIVES} attempts remaining to guess the number.")
        choice = int(input("Make a guess: "))

        if choice < NUMBER:
            LIVES -= 1
            print("Too Low")

        if choice > NUMBER:
            LIVES -= 1
            print("Too High")

        if choice == NUMBER:
            print(f"You got it! The answer was: {choice}")
            print("\nThanks for playing")
            LIVES = 0



print("\nWelcome to the Number Guessing Name!\n   Im Thinking of a number between 1 at 100...")
NUMBER = random.randint(1, 100)
print(f"    The correct number is: {NUMBER}\n")
EASY_OR_HARD = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

start = True
while start:
    LIVES = 0

    if EASY_OR_HARD == "easy":
        easy()
        start = False

    if EASY_OR_HARD == "hard":
        hard()
        start = False

""" EXPLICACIÓN DE MI CODIGO
# Importa el logo del juego desde el archivo 'art.py'
from art import logo
# Importa el módulo 'random' para generar un número aleatorio
import random

# Muestra el logo del juego
print(logo)

# Define la función para el modo fácil
def easy():
    # Usa variables globales para que puedan ser leídas y modificadas fuera de la función
    global NUMBER
    global LIVES
    # Establece 10 vidas para el modo fácil
    LIVES = 10

    # Mientras queden vidas, el jugador puede seguir intentando
    while LIVES > 0:
        # Muestra cuántas vidas le quedan al jugador
        print(f"\nYou have {LIVES} attempts remaining to guess the number.")
        # Solicita un número al jugador y lo convierte a entero
        choice = int(input("Make a guess: "))

        # Si el número ingresado es menor al número correcto
        if choice < NUMBER:
            LIVES -= 1  # Resta una vida
            print("Too Low")  # Informa que el número es muy bajo

        # Si el número ingresado es mayor al número correcto
        if choice > NUMBER:
            LIVES -= 1  # Resta una vida
            print("Too High")  # Informa que el número es muy alto

        # Si el número es correcto
        if choice == NUMBER:
            print(f"You got it! The answer was: {choice}")  # Felicita al jugador
            print("\nThanks for playing")  # Mensaje de agradecimiento
            LIVES = 0  # Finaliza el juego saliendo del ciclo

# Define la función para el modo difícil (similar a easy pero con menos vidas)
def hard():
    global NUMBER
    global LIVES
    LIVES = 5  # Solo 5 intentos en modo difícil

    while LIVES > 0:
        print(f"\nYou have {LIVES} attempts remaining to guess the number.")
        choice = int(input("Make a guess: "))

        if choice < NUMBER:
            LIVES -= 1
            print("Too Low")

        if choice > NUMBER:
            LIVES -= 1
            print("Too High")

        if choice == NUMBER:
            print(f"You got it! The answer was: {choice}")
            print("\nThanks for playing")
            LIVES = 0

# Muestra mensaje de bienvenida
print("\nWelcome to the Number Guessing Name!\n   Im Thinking of a number between 1 at 100...")

# Genera un número aleatorio entre 1 y 100
NUMBER = random.randint(1, 100)
# Muestra el número (para pruebas o depuración, puedes quitarlo después)
print(f"    The correct number is: {NUMBER}\n")

# Pide al usuario que elija una dificultad ('easy' o 'hard')
EASY_OR_HARD = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Variable de control para iniciar el juego
start = True

# Bucle principal del juego
while start:
    LIVES = 0  # Reinicia el contador de vidas antes de entrar a la función

    # Si el usuario eligió modo fácil
    if EASY_OR_HARD == "easy":
        easy()      # Llama a la función easy
        start = False  # Finaliza el bucle del juego

    # Si el usuario eligió modo difícil
    if EASY_OR_HARD == "hard":
        hard()      # Llama a la función hard
        start = False  # Finaliza el bucle del juego

"""