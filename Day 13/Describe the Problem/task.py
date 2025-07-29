def my_function():
    for i in range(1, 20):        # El bucle for itera para i en un rango de 1 hasta 19 (No se toma el extremo 20)
        if i == 20:               # Si i es igual 20 entonces...
            print("You got it")   # Nunca imprímira ya que nuna llegara a 20


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?

# CORRECCIÓN ...
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()