print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
factura = 0 #Inicializamos la factura en 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        factura = 5
        print("Please pay $5.")
    elif age <= 18:
        factura = 7
        print("Please pay $7.")
    else:
        factura = 12
        print("Please pay $12.")

    Foto =int(input("Desea añadir una foto por $3 USD adicionales?\nMarque 1 para Sí y 2 para No:\n"))
    if Foto == 1:
        factura += 3

    print(f"Su factura Total es: $ {factura}")
else:
    print("Sorry you have to grow taller before you can ride.")
