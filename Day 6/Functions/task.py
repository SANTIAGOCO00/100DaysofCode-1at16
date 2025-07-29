# FUNCIONES: Crearemos nuestras propias funciones, similar a print(), len(), etc..
# SOLO SE ACTIVARAN CUANDO SEAN LLAMADAS

def my_function(): # Creamos nuestra función...
    print("Hello") # Dentro del bloque de la función crearemos los parametros
    print("Bye")   # Estos no se imprimiran hasta que se llame la función
my_function() # LLamamos nuestra función que ejecutara los parametros

# while - mientras sea verdadero entra en bucle
""" https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


obstaculos = 6
while obstaculos > 0:
    jump()
    obstaculos -= 1
    print(obstaculos)
"""