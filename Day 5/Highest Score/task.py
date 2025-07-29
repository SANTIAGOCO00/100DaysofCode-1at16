# Sumando datos de una lista
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# Usamos sum() para sumar cada objeto en la lista y el resultado se guarda en una nueva variable llamada score
score = sum(student_scores)
print(f"La suma de la lista es: {score}")

# Otro metodo pero con bucles y menos eficiente...
suma = 0 # Inicializamos una variable que almacenara la suma
for student in student_scores: # Creamos una variable que almacenara uno a uno los datos de lista
    suma += student # La variable sum almacena y suma los datos de student

print(f"\nLa suma de la lista es {suma}") # Imprimimos Fuera del bucle para no iterar

#________________________________________________________________________________________________________________
print(f"\nReplicar con bucles la función max en la misma lista {student_scores}")
max_score = max(student_scores)
print(f"max() busca el numero mayor en una lista, en este caso es: {max_score}")

# Otro metodo pero primitivo...
max_score = 0 # Inicializamos una variable en 0
for number in student_scores:  # Creamos una variable que almacenara uno a uno los datos de lista
    if number > max_score: # if(si) numero es mayor que nuestra variable iniciada en 0
        max_score = number # La variable iniciada en cero sera igual al número

print(f"El puntaje maximo con un metodo primitivo es: {max_score}")
