# Parametro: Nombre de los argumentos que se reciben del argumento
def greet(a): # a es un parametro que luego heredara un argumento...
    print(f"Hola! {a}")
    print("Como se encuentra el dia de hoy? ")
    print("Que tal el clima en donde esta?")

name = input("Whats your name?\n")
# Argumento: Va dentro del parentesis cuando se llama la función, y envia los datos al parametro
greet(name) # Es el argumento que se envia al parametro a

