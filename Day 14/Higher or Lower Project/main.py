import random
import game_data
import art
print(art.logo)

def compare(num_a, num_b):
    if num_a > num_b:
        return "a"
    if num_a < num_b:
        return "b"
    else:
        return 'c'


score = 0
start = True
while start:

    A_OPTION = random.choice(game_data.data)
    A_FOLLOWERS = A_OPTION["follower_count"]
    print(f"\nCompare A: {A_OPTION["name"]}, a {A_OPTION["description"]}, from {A_OPTION["country"]}.")

    print(f"{art.vs}")

    B_OPTION = random.choice(game_data.data)
    B_FOLLOWERS = B_OPTION["follower_count"]
    print(f"\nAgainst B: {B_OPTION["name"]}, a {B_OPTION["description"]}, from {B_OPTION["country"]}.")
    A_OR_B = input("Who has more followers? Tpe 'A' or 'B' : ").lower()

    ANSWER = compare(A_FOLLOWERS, B_FOLLOWERS)

    if ANSWER == A_OR_B:
        score += 1
        print(f"You're right! Current score {score}")

    else:
        print(f"Sorry, that's wrong. Final score {score}")
        start = False
