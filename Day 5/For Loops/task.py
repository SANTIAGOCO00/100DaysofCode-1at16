# Bucles - Lopps
# for - in

fruits = ["Apple", "Peach", "Pear"]
print(f"\nNuestra lista es {fruits}")
for fruit in fruits: # Creamos una nueva varible llamada fruit para fruits
    print(fruit) # Imprime los items de la lista en vertical uno a uno

print("\nImprime los items de la lista en vertical uno a uno y añade la cadena a cada item")
for fruit in fruits:  # Creamos una nueva varible llamada fruit para fruits
    print(fruit + " " + "Strawberry") # Imprime los items de la lista en vertical uno a uno y añade la cadena a cada item

print("\nImprime la lista - NOTA: En este caso NO usamos la varible fruit, solo usamos la lista")
for fruit in fruits:  # Creamos una nueva varible llamada fruit para fruits
    print(fruits) # Imprime la lista - NOTA: En este caso no usamos la varible fruit, solo usamos la lista

# Ahora todo junto...
fruits = ["Apple", "Peach", "Pear"]
print("\nAhora todo junto...")
for fruit in fruits: # Creamos una nueva varible llamada fruit para fruits
    print(fruit) # Imprime los items de la lista en vertical uno a uno
    print(fruit + " " + "Strawberry")  # Imprime los items de la lista en vertical uno a uno y añade la cadena a cada item
    print(fruits)  # Imprime la lista - NOTA: En este caso no usamos la varible fruit, solo usamos la lista