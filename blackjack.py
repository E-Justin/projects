# this program will be a working blackjack game

import random

suits = ['spades', 'hearts', 'diamonds', 'clubs']

values = ['2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'Jack', 'Queen', 'King', 'Ace']

users_hand = []
dealers_hand = []


def get_game_deck(s: list[str], v: list[str]) -> list[str]:
    """ this function takes suits as the first argument and card values as the second
        this function builds a deck of 52 cards (4 of each suit) and returns the deck as a list"""
    deck = []  # local variable to hold all 52 card values
    for s in range(len(suits)):  # iterates through each suit
        for v in range(len(values)):  # iterates through each card for each suit
            # appends each card and suit to the game_deck variable
            deck.append('%s of %s' % (values[v], suits[s]))
    return deck  # returns the full game deck


# assign the game deck to the game_deck variable
game_deck = get_game_deck(suits, values)

random.shuffle(game_deck)  # shuffle the cards randomly


def get_cards(deck_of_cards: list[str]) -> list[str]:
    """ this function gets two random cards from the deck
        takes a list of strings (the game deck) as an argument
        returns player's hand of two cards"""
    cards = []
    length = len(deck_of_cards)
    card1_index = random.randint(0, length - 1)  # get first card's index
    card1 = deck_of_cards[card1_index]  # assign card1 to variable
    # remove card1 from the deck (so there are no repeats)
    deck_of_cards.remove(deck_of_cards[card1_index])
    cards.append(card1)  # give card to player

    card2_index = random.randint(0, length - 1)  # get second card's index
    card2 = deck_of_cards[card2_index]  # assign card2 to variable
    # remove card2 from the deck (so there are no repeats)
    deck_of_cards.remove(deck_of_cards[card2_index])
    cards.append(card2)  # give card to player

    return cards


def hit_me(a_players_hand: list[str], deck_of_cards: list[str]) -> str:
    """ this function appends another random card to the player's hand
        and returns the new card"""
    length = len(deck_of_cards)  # get length (it changes when a card is dealt)
    # get next card's random index
    next_card_index = random.randint(0, length - 1)
    next_card = deck_of_cards[next_card_index]  # get next card
    deck_of_cards.remove(next_card)  # remove it from the deck
    return next_card


users_hand = get_cards(game_deck)  # deal cards to user
dealers_hand = get_cards(game_deck)  # deal cards dealer


def total_up_hand(a_players_hand: list[str]) -> int:
    """ this function totals up the amount of points for a player's hand
        takes a player's hand as an argument and returns their total """
    first_value = a_players_hand[0][0]


def game_menu():
    """ this function displays the game menu and handles user input"""
    while True:
        print('Your current hand : %s\n' % (users_hand))
        # print(users_hand[0][0])
        # print(users_hand[1][0])
        print('1) .... Hit me ')
        print('2) .... Stay ')
        print('3) .... Exit Game')
        menu_selection = input('Select from the menu... \n')  # gets user input
        if menu_selection == '1':  # 'hit me '
            # append new card to users hand and remove it from the deck
            users_hand.append(hit_me(users_hand, game_deck))
        else:
            print('Goodbye')
            break


game_menu()

#! to do:
#! what happens when user busts
#! function to total up the points (for numbers and face cards)
#! show dealer's cards
#! betting?
#! if statement to handle 'stay'
#! win/ losses/ ties displayed
