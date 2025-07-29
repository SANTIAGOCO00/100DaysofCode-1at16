""" CORREGIR ESTE CÓDIGO CON ERRORES OCASIONALES
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994: # Debería ser if
    print("You are a Gen Z.")
# Falta else
"""


year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994: # Añadimos = para que se incluyan las personas de 1994, en algún grupo
    print("You are a Gen Z.")
# Falta else