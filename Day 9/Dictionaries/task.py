
# Diccionario: Key - Value
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}


# Para mostrar un elemento del diccionario debemos usar la llave
# Usamos un método similar a una lista
# Y lo mostramos con print()
print(programming_dictionary ["Bug"])
# La salida será la definición de la llave Bug


# Para editar una el value ana Key será de la siguiente manera...
programming_dictionary ["Bug"] = "Is a insect."
# Imprimimos tdo el diccionario para como quedo...
print(programming_dictionary)


# Para añadir una nueva key-value al diccionario se hará de la siguiente manera...
programming_dictionary ["Loop"] = "The action of doing something over and over again."
# Imprimimos tdo el diccionario para como quedo...
print(programming_dictionary)

# Bucle for con diccionarios
for key in programming_dictionary:
    print(key) # SALIDA: Nos dara todas las llaves del diccionario...
    print(programming_dictionary[key]) # También podemos pasar las llaves al diccionario
                                       # para mostrar los valores de cada una

# Para borrar un diccionario por completo podemos usar = {}
programming_dictionary = {}
# Imprimimos tdo el diccionario para como quedo...
print(programming_dictionary) # SALIDA: {}