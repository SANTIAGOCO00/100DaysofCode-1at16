# Listas - List
states_of_america = ["Delawere", "Pensylvania", "hawai"]
print(states_of_america[1]) # Buscamos con el indice [] en la lista
states_of_america[1] = "Miami" # Remplazamos el valor indicado en el indice []
print(states_of_america)

# __________________________
states_of_america.append("Santiago") #Añade un elemento al final de lista
print(states_of_america)
states_of_america.extend(["Oscar", "Lina"]) #Añade un varios elementos al final de lista
print(states_of_america)