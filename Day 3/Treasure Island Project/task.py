print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n Elige entre dos opciones. 1 o 2 para interactuar")
print("Your mission is to find the treasure.")
chose1 = int(input("Bienvenido aventurero, tenemos que saltar del bote...\n Elije entre 1 (Saltar al agua) o 2 (Esperar en el bote)\n"))
if chose1 == 1:
    chose2 = int(input("Estamos en el agua!! Que hacemos??? Nadamos o Esperamos...\n Para nadar 1 / Para esperar 2\n"))
    if chose2 == 2:
        chose3 = int(input("Oh no, Carlos esta nadando. Y lo ataco un tiburon, menos mal esperamos un poco mas...\n Aparecen tres botes de diferentes colores!!!\n Cual elejimos Capitan?? 1 para el rojo, 2 para el amarillo y 3 para el azul\n"))
        if chose3 == 2:
            print("Despues de unos dias por fin volvemos a casa...\n Sobreviviste")
        elif chose3 == 3:
            print("Nunca llegamos a tierra y nos hemos empezado a morir de hambre...\n Has muerto de hambre")
        elif chose3 == 1:
            print("Nuestro bote se ha hundido poco a poco y no tenemos fuerzas para nadar...\n Te han comido los tiburones")
        else:
            print("Nos hemos cansado de y no podemos resistir en el agua por mucho tiempo...\n Te has ahogado")
    else:
        print("Vamos nadando, Oh no!!! Un tiburon me muerde!!! AYUDAAAA!!!\n Has muerto...")
else:
    print("Game over... Te a succionado el remolino junto al bote")

