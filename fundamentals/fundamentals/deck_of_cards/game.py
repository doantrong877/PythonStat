from classes.deck import Deck
import random

bicycle = Deck()

#bicycle.show_cards()


"""
- create players
- deal card to players
-ask player 1 if want to draw more card
-ask player 2 if want to draw more card
"""
def black_jack():
    players = {}
    card_deck = bicycle.get_deck()
    name1 = input("Player 1 please enter your name: ")
    players[name1] = []
    name2 = input("Player 2 please enter your name: ")
    players[name2] = []

    #deal cards 1
    for i in range(2):
        random_card = random.choice(card_deck)
        card_deck.remove(random_card)
        players[name1].append(random_card)
    for i in range(2):
        random_card = random.choice(card_deck)
        card_deck.remove(random_card)
        players[name2].append(random_card)

    while True:
        player1_turn = input(f"hey {name1} do press 'y' to draw more card or 'n' to skip turn")
        if player1_turn == 'y':
            random_card = random.choice(card_deck)
            card_deck.remove(random_card)
            players[name1].append(random_card)
            for i in range(len(players[name1])):
                print(f"{players[name1][i].get_card()}")
            continue
        else:
            break

    while True:
        player2_turn = input(f"hey {name2} do press 'y' to draw more card or 'n' to skip turn")
        if player2_turn == 'y':
            random_card = random.choice(card_deck)
            card_deck.remove(random_card)
            players[name1].append(random_card)
            for i in range(len(players[name2])):
                print(f"{players[name1][i].get_card()}")
            continue
        else:
            break 




   # print(f"{players[name1][0].get_card()} {players[name1][0].get_value()}")
black_jack()