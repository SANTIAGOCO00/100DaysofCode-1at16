import art
print(art.logo)


def mejor_postor(diccionario):
    winner = ""
    highest_price = 0
    for keys in diccionario:
        contador_price = diccionario[keys]
        if contador_price > highest_price:
            highest_price = contador_price
            winner = keys

    print(f"The winner is {winner} with: $ {highest_price}")

data = {}
start = True
while start:
    name = input("What is your name?:\n").lower()
    price = float(input("What is your bid?:\n$ "))
    data[name] = price
    yes_or_no = input("Are there any other bidders?\n   Type Yes or No...\n").lower()
    if yes_or_no == "no":
        start = False
        mejor_postor(data)
    else:
        print("\n" * 20)
        start = True