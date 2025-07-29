bmi = 84 / 1.65 ** 2 # Salida:

print(bmi) # Salida: 30.85399449035813 (No es buena idea mostrar tantos números al usuario)

print(int(bmi)) # Salida: 30 (No es buena idea mostrar un número entero en números cientificos)

# round(number, ndigits) - Mejor opción de salida round() redondea al entero mas cercano
print(round(bmi)) # Salida: 31
# Tambien buena opción
print(round(bmi,2)) # Salida: 30.85 (Salida sin redondear mostrando unos pocos decimales)
#________________________________________________________________________________________________________________

# OPERADORES DE ASIGNACIÓN
# Añadir operaciones a las variables
SCORE = 0
SCORE += 1
SCORE -= 2
SCORE *= 3
SCORE /= 4
print(SCORE) # Salida:  -0.75

# f string (f""{})
# Insertar una variable o una expresion dentro de una cadena de texto mucho mas optimo
age = 12
print(f"Tengo {age} años de edad") # Salida: Tengo 12 años de edad
