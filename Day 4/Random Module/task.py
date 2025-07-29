import random

random_integrer = random.randint(1 , 10)
print(random_integrer)

# _______________________________________________
# Usando Random.random()
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

#________________________________________________
# Usando Random.random() pero multiplicando
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

#________________________________________________
# Usando random.uniform()
random_float = random.uniform(1,10)
print(random_float)

# _______________________________________________
#Creamos y usamos un modulo en otra pestaña
import my_module
print(my_module.my_favorite_number)
#________________________________________________

print("Actividad...")
heads_or_tails = random.randint(0, 1)
if heads_or_tails == 0:
    print("heads")
else:
    print("tails")