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

    return cards  # returns two random cards out of the deck


def hit_me(a_players_hand: list[str], deck_of_cards: list[str]) -> str:
    """ this function appends another random card to the player's hand
        and returns the new card"""
    length = len(deck_of_cards)  # get length (it changes when a card is dealt)
    # get next card's random index
    next_card_index = random.randint(0, length - 1)
    next_card = deck_of_cards[next_card_index]  # get next card
    deck_of_cards.remove(next_card)  # remove it from the deck

    return next_card  # returns another random card from the deck


users_hand = get_cards(game_deck)  # deal cards to user
dealers_hand = get_cards(game_deck)  # deal cards dealer


def total_up_hand(a_players_hand: list[str]) -> int:
    """ this function totals up the amount of points for a player's hand
        takes a player's hand as an argument and returns their total """

    card3_value = 0
    card4_value = 0
    card5_value = 0

    length = len(a_players_hand)  # get total number of cards in hand

    card1 = a_players_hand[0].split(
        ' ')  # split the string into a list for indexing
    card1 = card1[0]  # get first word of list ('King', '6', 'Ace'...)

    # split the string into a list for indexing
    card2 = a_players_hand[1].split(' ')
    card2 = card2[0]  # get first word of list ('King', '6', 'Ace'...)

    if length > 2:
        # split the string into a list for indexing
        card3 = a_players_hand[2].split(' ')
        card3 = card3[0]  # get first word of the list ('King', '6', 'Ace'...)
    if length > 3:
        # split the string into a list for indexing
        card4 = a_players_hand[3].split(' ')
        card4 = card4[0]  # get first word of the list ('King', '6', 'Ace'...)
    if length > 4:
        # split the string into a list for indexing
        card5 = a_players_hand[4].split(' ')
        card5 = card5[0]  # get first word of the list ('King', '6', 'Ace'...)

    # if it is not a face card, get the value of the card
    card1_value = values.index(card1) + 2
    if card1_value >= 11 and card1_value <= 13:  # if it is a face card other than Ace
        card1_value = 10  # value == 10
    elif card1_value == 14:  # if it is an Ace
        card1_value = 11  # value is 11

    # if it is not a face card, get the value of the card
    card2_value = values.index(card2) + 2
    if card2_value >= 11 and card2_value <= 13:  # if it is a face card other than Ace
        card2_value = 10  # value == 10
    elif card2_value == 14:  # if it is an Ace
        card2_value = 11  # value is 11

    if length > 2:  # if they have 3 or more cards in their hand
        card3_value = values.index(card3) + 2
        if card3_value >= 11 and card3_value <= 13:  # if it is a face card other than Ace
            card3_value = 10  # value == 10
        elif card3_value == 14:  # if it is an Ace
            card3_value = 11  # value is 11

    if length > 3:  # if they ahve 4 or more cards in their hand
        card4_value = values.index(card4) + 2
        if card4_value >= 11 and card4_value <= 13:  # if it is a face card other than Ace
            card4_value = 10  # value == 10
        elif card4_value == 14:  # if it is an Ace
            card4_value = 11  # value is 11

    if length > 4:  # if they have 5 cards or more in their hand
        card5_value = values.index(card5) + 2
        if card5_value >= 11 and card5_value <= 13:  # if it is a face card other than Ace
            card5_value = 10  # value == 10
        elif card5_value == 14:  # if it is an Ace
            card5_value = 11  # value is 11

    total = card1_value + card2_value + card3_value + \
        card4_value + card5_value  # get total

    if total == 21 and length == 2:  # if the user gets blackjack
        print(' ***** Blackjack! ****** ')
    elif total > 21:  # if the player busts
        print(' ----- Bust! ------ ')
    else:
        print('Your current total is : %d ' % total)  # show player's total

    return total  # return total


def game_menu():
    """ this function displays the game menu and handles user input"""
    while True:
        print('Your current hand : %s\n' % (users_hand))
        print('1) .... Hit me ')
        print('2) .... Stay ')
        print('3) .... Exit Game')
        menu_selection = input('Select from the menu... \n')  # gets user input
        if menu_selection == '1':  # 'hit me '
            # append new card to users hand and remove it from the deck
            users_hand.append(hit_me(users_hand, game_deck))
            total_up_hand(users_hand)
        elif menu_selection == '2':  # 'stay'
            total_up_hand(users_hand)
        else:
            print('Goodbye')
            break


game_menu()

#! to do:
#! ace == 11 or 1 (now it is only 11)
#! what happens when user busts
#! show dealer's cards
#! betting?
#! if statement to handle 'stay'
#! win/ losses/ ties displayed
