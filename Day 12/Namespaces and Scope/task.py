enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
#________________________________________________________________________________

enemigos = 1


def increase_enemies():
    global enemigos
    enemigos += 1
    print(f"enemies inside function: {enemigos}")


increase_enemies()
print(f"enemies outside function: {enemigos}")
