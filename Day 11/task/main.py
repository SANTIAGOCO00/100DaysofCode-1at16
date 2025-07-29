import art
import random


def calculate_score(list1, list2):
    final_user = sum(list1)
    print(f"Your final hand is {list1}, final score: {final_user} ")
    final_pc = sum(list2)
    print(f"Computer final hand is: {list2}, final score {final_pc}")

    if final_user > 21:
        return "You Lose"

    if final_user <= 21 and final_pc > 21:
        return "You Win"

    if final_user > final_pc:
        return "You win"

    if final_pc > final_user:
        return "You Lose"

    if final_user == final_pc:
        return "Its a Draw"

    else:
        return "You Lose"




yes_or_no = input(f"Do you want to play a game of BlackJack? Type 'y' or 'n' :\n").lower()
while yes_or_no == "y":
    print(art.logo)

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    pc_cards = []

    for _ in range(2):
        carta = random.choice(cards)
        cards.remove(carta)
        user_cards.append(carta)
    total_user = sum(user_cards)
    print(f"Your cards: {user_cards}, current score {total_user}")

    for _ in range(2):
        carta = random.choice(cards)
        cards.remove(carta)
        pc_cards.append(carta)
    print(f"Computer first card: {pc_cards[0]}")

    anothercard = input(f"Type 'y' to get another card, Type 'n' to pass:\n").lower()
    if anothercard == "y":
        carta = random.choice(cards)
        cards.remove(carta)
        user_cards.append(carta)
    total_user = sum(user_cards)
    print(f"Your cards: {user_cards}, current score {total_user}")
    print(calculate_score(user_cards, pc_cards))

    if anothercard == "n":
        print(calculate_score(user_cards, pc_cards))
        yes_or_no = "n"
        print("\n" * 20)

