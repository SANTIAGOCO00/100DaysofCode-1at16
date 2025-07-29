print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    edad = int(input("You can ride the rollercoaster!\n Cual es su edad?"))
    if edad <= 12:
        print("Debera pagar $ 5 USD ")
    elif edad <= 18:
        print("Debera pagar $ 7 USD ")
    else:
        print("Debera pagar $ 12 USD")
else:
    print("Sorry you have to grow taller before you can ride.")