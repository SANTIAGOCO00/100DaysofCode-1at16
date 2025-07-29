# Range() - asignamos un rango para recorrer dentro de una lista
# El rango incluye el limite inferior pero no el limite superior

# Suma de los números del 1 al 100...
suma = 0 # inicializamos una variable en 0
for numbers in range(1,101): # Le asignamos a la variable numbers en rango de número de 1 a 100
    suma += numbers # Suma el valor de su derecha a la variable de su izquierda y asigna el resultado a la variable de su izquierda
print(f"La suma de los números del uno al 100 es {suma}") # Imprimimos
#_______________________________________________________________________________________________________________________
"""FizzBuzz
Vas a escribir un programa que imprima automáticamente la solución del juego FizzBuzz. Estas son las reglas del juego FizzBuzz:

Tu programa debe imprimir cada número del 1 al 100, uno por uno, incluyendo el 100.

Pero si el número es divisible entre 3, en lugar del número, debe imprimir "Fizz".

Si el número es divisible entre 5, en lugar del número, debe imprimir "Buzz".

Y si el número es divisible entre 3 y 5 (por ejemplo, 15), en lugar del número, debe imprimir "FizzBuzz"."""

suma = 0
for numbers in range(1,101):
    if suma == numbers % 3 and suma == numbers % 5:
        print("FizzBuzz")
    elif suma == numbers % 3:
        print("Fizz")
    elif suma == numbers % 5:
        print("Buzz")

    else:
        print(numbers)