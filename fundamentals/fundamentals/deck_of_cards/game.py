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
    print(f"{name1} card")
    for i in range(len(players[name1])):
        print(f"{players[name1][i].get_card()}") 
    print(f"{name2} card")
    for i in range(2):
        random_card = random.choice(card_deck)
        card_deck.remove(random_card)
        players[name2].append(random_card)
    for i in range(len(players[name2])):
                print(f"{players[name2][i].get_card()}")
    while True:
        player1_turn = input(f"hey {name1} do press 'y' to draw more card or 'n' to skip turn: ")
        if player1_turn == 'y':
            random_card = random.choice(card_deck)
            card_deck.remove(random_card)
            players[name1].append(random_card)
            for i in range(len(players[name1])):
                print(f"{players[name1][i].get_card()}")
            continue
        elif player1_turn == 'n':
            break

    while True:
        player2_turn = input(f"hey {name2} do press 'y' to draw more card or 'n' to skip turn: ")
        if player2_turn == 'y':
            random_card = random.choice(card_deck)
            card_deck.remove(random_card)
            players[name1].append(random_card)
            for i in range(len(players[name2])):
                print(f"{players[name2][i].get_card()}")
            continue
        elif player2_turn == 'n':
            break 


    #compare card
    player1_point = 0
    for i in range(len(players[name1])):
        if players[name1][i].get_value() >= 10:
            player1_point += 10
            continue
        else:
            player1_point += players[name1][i].get_value()
    print(f"{name1} total point {player1_point}")
    player2_point = 0
    for i in range(len(players[name2])):
        if players[name2][i].get_value() >= 10:
            player2_point += 10
            continue
        else:
            player2_point += players[name2][i].get_value()
    print(f"{name2} total point {player2_point}")
    #The winner is

    if player1_point <= 21 and player2_point <= 21:
        if player1_point > player2_point:
            print(f"{name1} is the winner")
        elif player1_point < player2_point:
            print(f"{name2} is the winner")
        else:
            print("it a draw")
    elif player1_point >= 21 and player2_point >= 21:
        print("it a draw")
    elif  player1_point >= 21 and player2_point <= 21:
        print(f"{name2} is the winner")
    else:
        print(f"{name1} is the winner")

   # print(f"{players[name1][0].get_card()} {players[name1][0].get_value()}")
black_jack()