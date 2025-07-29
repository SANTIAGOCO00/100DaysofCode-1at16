import random # Permite usar funciones de azar

# Creamos las listas que usaremos...
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Solicitamos al usuario cuantos caracteres quiere...
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password1 = [] # Creamos una lista vacía, donde iremos guardando las letras seleccionadas aleatoriamente. Para luego barajarlos


# AGREGAR LETRAS ALEATORIAS

# _ Significa: Si necesito repetir esto pero no me importa el valor de la variable
for _ in range(nr_letters):                 # Repetimos el siguiente bloque de código 'nr_letters' veces (es decir, tantas veces como letras debe tener la contraseña)
    letras = random.choice(letters)         # Elegimos una letra al azar de la lista 'letters' y asignamos a una nueva variable
    password1 += letras                     # Agregamos esas letras una a una la lista 'password1'
print(f"Letras seleccionadas: {password1}") # Imprimimos fuera del bucle para obtener solo el resultado final


# AGREGAR SÍMBOLOS ALEATORIOS

for _ in range(nr_symbols):
    symbolos = random.choice(symbols)
    password1 += symbolos
print(f"+ Simbolos seleccionadas: {password1}")


# AGREGAR NÚMEROS ALEATORIOS

for _ in range(nr_numbers):
    numeros = random.choice(numbers)
    password1 += numeros
print(f"+ Números seleccionadas: {password1}")

random.shuffle(password1) # USAMOS SHUFFLE PARA BARAJAR UNA LISTA

# "" Indica que queremos unir strings sin espacios intermedios
password = ""        # Inicializamos una variable de texto vacía y pasamos nuestra lista al nuevo bucle para convertirlo a texto
# i es un contador o indice
for i in password1:  # Recorremos la lista password1, caracter por caracter
    password += i    # Suma cada caracter a la string vacia

print(f"\nSu contraseña es: {password}") # MOSTRAR LA CONTRASEÑA FINAL.

""" 
# CÓDIGO DE ANGELA YU
# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level
# password = ""

# for char in range(1, nr_letters + 1):
#   password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#   password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password += random.choice(numbers)

# print(password)

#Hard Level
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
"""