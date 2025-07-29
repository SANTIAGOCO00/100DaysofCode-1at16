import random

Player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
Game = ["Rock", "Paper", "Scissors"]
choice_pc = random.randint(0, 2)
print(f"El Pc ha elejido: {Game[choice_pc]}")
print(f"Tu has elejido: {Game[Player]}")

if Player >= 3 or Player <0:
    print("Seleccione una opción correcta por favor")
elif choice_pc == 0 and Player == 2:
    print("Ha perdido")
elif choice_pc == 2 and Player == 0:
    print("Ha ganado")
elif choice_pc > Player:
    print("Has perdido")
elif choice_pc < Player:
    print("Has ganado")
elif choice_pc == Player:
    print("Es un empate")
