import main

AGUA = main.resources["water"]
LECHE = main.resources["milk"]
CAFE = main.resources["coffee"]
INGRESOS = 0

# Espresso
AGUA_ESPRESSO = main.MENU["espresso"]["ingredients"]["water"]
CAFE_ESPRESSO = main.MENU["espresso"]["ingredients"]["coffee"]
COSTO_ESPRESSO = main.MENU["espresso"]["cost"]

# Latte
AGUA_LATTE = main.MENU["latte"]["ingredients"]["water"]
LECHE_LATTE = main.MENU["latte"]["ingredients"]["milk"]
CAFE_LATTE = main.MENU["latte"]["ingredients"]["coffee"]
COSTO_LATTE = main.MENU["latte"]["cost"]

# Cappuccino
AGUA_CAPPUCCINO = main.MENU["cappuccino"]["ingredients"]["water"]
LECHE_CAPPUCCINO = main.MENU["cappuccino"]["ingredients"]["milk"]
CAFE_CAPPUCCINO = main.MENU["cappuccino"]["ingredients"]["coffee"]
COSTO_CAPPUCCINO = main.MENU["cappuccino"]["cost"]


start = True
while start:
    print(main.logo)
    print("\nBienvenido a Santiago's Coffe Machine software")
    ORDEN = input("Que desea ordenar? Tenemos...\nEspresso\nLatte\nCappuccino\n   Ingrese su orden: ").lower()


    if ORDEN == "recursos":
        print(f"    La cafeteria contiene los siguientes recursos...\n"
              f"    agua {AGUA}ml\n"
              f"    leche {LECHE}ml\n"
              f"    cafe {CAFE}g\n"
              f"    Ingresos {INGRESOS} USD")

    if ORDEN == "espresso":
        print(f"    El espresso contiene los siguientes ingredientes...\n"
              f"    agua {AGUA_ESPRESSO}ml\n"
              f"    cafe {CAFE_ESPRESSO}g\n"
              f"    TIENE UN COSTO DE {COSTO_ESPRESSO} USD\n")
        if AGUA_ESPRESSO > AGUA:
            print("     No tenemos suficiente agua para su espresso...")
        elif CAFE_ESPRESSO > CAFE:
            print("     No tenemos suficiente cafe para su espresso...")
        else:
            print("Ingrese por favor su pago...")
            PENNIES = float(input("Pennies : "))
            DIMES = float(input("Dimes : "))
            NICKELS = float(input("Nickles : "))
            QUARTERS = float(input("Quarters : "))
            USD = (PENNIES * 0.01) + (NICKELS * 0.05) + (DIMES * 0.10) + (QUARTERS * 0.25)
            if USD >= COSTO_ESPRESSO:
                AGUA -= 50
                CAFE -= 18
                CAMBIO = USD - COSTO_ESPRESSO
                INGRESOS += COSTO_ESPRESSO
                print(f"Su cambio es: {CAMBIO}")
                print("\nEsperamos que disfrute de su espresso :)")
            else:
                print(f"\nLo sentimos, fondos insuficientes...\n    Regreso dinero $ {USD} USD")


    if ORDEN == "latte":
        LATTE = main.MENU["latte"]
        print(f"    El latte contiene los siguientes ingredientes...\n"
              f"    agua {AGUA_LATTE}ml\n"
              f"    leche {LECHE_LATTE}ml\n"
              f"    cafe {CAFE_LATTE}g\n"
              f"    TIENE UN COSTO DE {COSTO_LATTE} USD\n")
        if AGUA_LATTE > AGUA:
            print("     No tenemos suficiente agua para su latte...")
        elif LECHE_LATTE > LECHE:
            print("     No tenemos suficiente leche para su latte...")
        elif CAFE_LATTE > CAFE:
            print("     No tenemos suficiente cafe para su latte...")
        else:
            print("Ingrese por favor su pago...")
            PENNIES = float(input("Pennies : "))
            DIMES = float(input("Dimes : "))
            NICKELS = float(input("Nickles : "))
            QUARTERS = float(input("Quarters : "))
            USD = (PENNIES * 0.01) + (NICKELS * 0.05) + (DIMES * 0.10) + (QUARTERS * 0.25)
            if USD >= COSTO_LATTE:
                AGUA -= 200
                LECHE -= 150
                CAFE -= 24
                CAMBIO = USD - COSTO_LATTE
                INGRESOS += COSTO_LATTE
                print(f"Su cambio es: {CAMBIO}")
                print("\nEsperamos que disfrute de su latte :)")
            else:
                print(f"\nLo sentimos, fondos insuficientes...\n    Regreso dinero $ {USD} USD")



    if ORDEN == "cappuccino":
        CAPPUCCINO = main.MENU["cappuccino"]
        print(f"    El cappuccino contiene los siguientes ingredientes...\n"
              f"    agua {AGUA_CAPPUCCINO}ml\n"
              f"    leche {LECHE_CAPPUCCINO}ml\n"
              f"    cafe {CAFE_CAPPUCCINO}g\n"
              f"    TIENE UN COSTO DE {COSTO_CAPPUCCINO} USD\n")
        if AGUA_CAPPUCCINO > AGUA:
            print("     No tenemos suficiente agua para su cappuccino...")
        elif LECHE_CAPPUCCINO > LECHE:
            print("     No tenemos suficiente leche para su cappuccino...")
        elif CAFE_CAPPUCCINO > CAFE:
            print("     No tenemos suficiente cafe para su cappuccino...")
        else:
            print("Ingrese por favor su pago...")
            PENNIES = float(input("Pennies : "))
            DIMES = float(input("Dimes : "))
            NICKELS = float(input("Nickles : "))
            QUARTERS = float(input("Quarters : "))
            USD = (PENNIES * 0.01) + (NICKELS * 0.05) + (DIMES * 0.10) + (QUARTERS * 0.25)
            if USD >= COSTO_CAPPUCCINO:
                AGUA -= 250
                LECHE -= 100
                CAFE -= 24
                CAMBIO = USD - COSTO_CAPPUCCINO
                INGRESOS += COSTO_CAPPUCCINO
                print(f"Su cambio es: {CAMBIO}")
                print("\nEsperamos que disfrute de su cappuccino :)")
            else:
                print(f"\nLo sentimos, fondos insuficientes...\n    Regreso dinero $ {USD} USD")

    if ORDEN == "off":
        print("Gracias por usar nuestros servicios, hasta la proxima")
        start = False
