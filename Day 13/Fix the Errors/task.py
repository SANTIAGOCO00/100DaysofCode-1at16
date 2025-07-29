""" CORREGIR ESTE CÓDIGO CON ERRORES OCASIONALES
age = int(input("How old are you?")) # Error si el usuario ingresa str en vez int
if age > 18:
    print("You can drive at age {age}.")
"""
# CORRECCIÓN CON MANEJO DE EXCEPCIONES: try - except

# try block
try: # Introducimos la parte del código que nos pueda dar error en algún momento
    age = int(input("How old are you?")) # Error si el usuario ingresa str en vez int

# Seguidamente usamos el bloque except ...
except ValueError: # Añadimos el nombre del error que nos pueda dar (lo podemos ver la terminal cuando ocurra el error)
    # Agregamos un comentario cuando ocurra el error ...
    print("Ingreso un número valido. Por favor digite solo caracteres numéricos sin símbolos")
    # Ejecutamos nuevamente él frágmento que nos pueda dar error
    age = int(input("How old are you?"))

    # Nota: En este caso solo funciona una vez. Usar while hasta que se cumpla la condición

if age > 18:
    print(f"You can drive at age {age}.")