import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card(hand, times=1):
    for _ in range(times):
        hand.append(random.choice(cards))


def calculate_score(hand):
    score = sum(hand)
    ace_count = hand.count(11)

    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1

    return score


want_to_continue = True

while want_to_continue:
    dealer_cards = []
    player_cards = []

    # Initial draw
    draw_card(dealer_cards, 2)
    draw_card(player_cards, 2)

    dealer_score = calculate_score(dealer_cards)
    player_score = calculate_score(player_cards)

    if dealer_score == 21 and player_score == 21:
        print("Dealer got a blackjack.You lose!")
        if input("Wanna play another game of blackjack? y/n: ").lower() == "n":
            want_to_continue = False
        else:
            print('\n'*10)
            continue

    if player_score == 21:
        print("Player got a blackjack.You win!")
        if input("Wanna play another game of blackjack? y/n: ").lower() == "n":
            want_to_continue = False
        else:
            print('\n'*10)
            continue


    print(f"Dealer's first card: {dealer_cards[0]}")
    print(f"Your cards: {player_cards} | score: {player_score}\n")

    # Player turn
    while player_score < 21:
        choice = input("Want to draw another card? y/n: ").lower()
        if choice != "y":
            break

        draw_card(player_cards)
        player_score = calculate_score(player_cards)
        print(f"Your cards: {player_cards} | score: {player_score}\n")

    # Player bust
    if player_score > 21:
        print("You busted. You lose!")
        print("\n" * 5)
    else:
        # Dealer turn
        while dealer_score < 17:
            draw_card(dealer_cards)
            dealer_score = calculate_score(dealer_cards)

        print(f"Dealer cards: {dealer_cards} | score: {dealer_score}")
        print(f"Your final score: {player_score}\n")

        # Result
        if dealer_score > 21:
            print("Dealer busted. You win!")
        elif player_score > dealer_score:
            print("You win!")
        elif player_score == dealer_score:
            print("Draw!")
        else:
            print("You lose!")

        print("\n" * 5)

    # Replay
    if input("Wanna play another game of blackjack? y/n: ").lower() == "n":
        want_to_continue = False
