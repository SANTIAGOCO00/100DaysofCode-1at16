print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S":
    bill += 15
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
