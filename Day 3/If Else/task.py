print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("Adelante! Puede subir a la atracción")
else:
    print("Lo sentimos, esta atracción esta restringida a tu altura por motivos de seguridad")

    bill = 0
    if size == "S":
        bill += 15
        print(f"La pizza Small tiene un valor de: {bill}")
        if pepperoni == "Y":
            bill += 2
            print(f"La adición de pepperoni tiene un valor de: $ {bill}")
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
    if size == "M":
        bill += 20
        print(f"La pizza Medium tiene un valor de: {bill}")
        if pepperoni == "Y":
            bill += 3
            print(f"La adición de pepperoni tiene un valor de: $ {bill}")
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")
    elif size == "L":
        bill += 25
        print(f"Your final bill is: ${bill}.")
        if pepperoni == "Y":
            bill += 3
            print(f"La adición de pepperoni tiene un valor de: $ {bill}")
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is: ${bill}.")