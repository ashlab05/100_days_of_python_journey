import random
import sys

import art
import game_data

print(art.logo)
print("Welcome to the Higher or Lower Game!")

while True:
    score = 0
    choice_1 = random.choice(game_data.data)

    game_on = True
    while game_on:
        choice_2 = random.choice(game_data.data)
        while choice_2 == choice_1:
            choice_2 = random.choice(game_data.data)

        print(
            f"{choice_1['name']}, {choice_1['description']}, from {choice_1['country']}"
        )
        print(art.vs)
        print(
            f"{choice_2['name']}, {choice_2['description']}, from {choice_2['country']}"
        )

        if choice_1["follower_count"] > choice_2["follower_count"]:
            winner = "a"
        else:
            winner = "b"
            choice_1 = choice_2

        user_guess = input("Enter your guess: A or B ? ").lower()

        if user_guess == winner:
            score += 1
            print(f"Correct! Your score: {score}")
        else:
            print(f"Wrong! Final score: {score}")
            if input("Do you want to play again? [Y/N] ").lower() != "y":
                sys.exit()
            game_on = False
