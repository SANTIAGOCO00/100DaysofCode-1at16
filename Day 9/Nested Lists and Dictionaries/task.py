# Anidamiento de listas y diccionarios

# Creamos nuestro diccionario Capitals
capitals = {
# Para vada Key el value va a ser una lista, paar tener varios valores en una llave
    "Brasil":["Samba","Bikiny","Portuguese"],
    "Venezuela":["Cancerbero","Miss Universe","Español"],
    "Colombia":["Vallenato","Cartagena","Bandeja Paisa"]
}

# Para imprimir únicamente de Venezuela: "Miss Universo" y no toda la lista...
print(capitals["Venezuela"][1])
#___________________________________________________________________________________________________

# Lista 2D (Lista dentro de otra lista)
# Creamos una lista con otra lista dentro...
nested_list = ["A","B",["C","D"]]

# Para imprimir únicamente la Letra "D" no laS dos listas...
print(nested_list[2][0])
#___________________________________________________________________________________________________

# Diccionario dentro de otro diccionario que también contiene una lista
# Creamos nuestro diccionario Fruits con el diccionario Acid
travel_log = {
    "France" : {
        "Num_times_visited":8,
        "Cities_visited":["Paris","Litle","Dijon"]
    },
    "Germany":{
        "Num_times_visited":8,
        "Cities_visited":["Stuttgart", "Hamburg", "Berlin"]
    }
}

# Para imprimir únicamente la Letra Berlin de este diccionario...
print(travel_log["Germany"]["Cities_visited"][2])