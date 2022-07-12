# this program will be a working blackjack game

import random

suits = ['spades', 'hearts', 'diamonds', 'clubs']

values = ['2', '3', '4', '5', '6', '7', '8',
          '9', '10', 'Jack', 'Queen', 'King', 'Ace']

users_hand = []
dealers_hand = []

tally = {
    "Wins": 0,
    "Losses": 0,
    "Ties": 0,
}


def get_game_deck(s: list[str], v: list[str]) -> list[str]:
    """ this function takes suits as the first argument and card values as the second
        this function builds a deck of 52 cards (4 of each suit) and returns the deck as a list"""
    deck = []  # local variable to hold all 52 card values
    for s in range(len(suits)):  # iterates through each suit
        for v in range(len(values)):  # iterates through each card for each suit
            # appends each card and suit to the game_deck variable
            deck.append('%s of %s' % (values[v], suits[s]))
    random.shuffle(deck)  # shuffle the cards randomly
    return deck  # returns the full game deck


# assign the game deck to the game_deck variable
game_deck = get_game_deck(suits, values)


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


def hit_me(deck_of_cards: list[str]) -> str:
    """ this function takes a game deck as an argument and returns a random card for appending"""
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

    hand_values = []

    total = 0

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
    hand_values.append(card1_value)

    # if it is not a face card, get the value of the card
    card2_value = values.index(card2) + 2
    if card2_value >= 11 and card2_value <= 13:  # if it is a face card other than Ace
        card2_value = 10  # value == 10
    elif card2_value == 14:  # if it is an Ace
        card2_value = 11  # value is 11
    hand_values.append(card2_value)

    if length > 2:
        card3_value = values.index(card3) + 2
        if card3_value >= 11 and card3_value <= 13:  # if it is a face card other than Ace
            card3_value = 10  # value == 10
        elif card3_value == 14:  # if it is an Ace
            card3_value = 11  # value is 11
        hand_values.append(card3_value)

    if length > 3:
        card4_value = values.index(card4) + 2
        if card4_value >= 11 and card4_value <= 13:  # if it is a face card other than Ace
            card4_value = 10  # value == 10
        elif card4_value == 14:  # if it is an Ace
            card4_value = 11  # value is 11
        hand_values.append(card4_value)

    if length > 4:
        card5_value = values.index(card5) + 2
        if card5_value >= 11 and card5_value <= 13:  # if it is a face card other than Ace
            card5_value = 10  # value == 10
        elif card5_value == 14:  # if it is an Ace
            card5_value = 11  # value is 11
        hand_values.append(card5_value)

    for num in hand_values:  # iterate through each number in
        total += num

    if total == 21 and length == 2:  # if the user gets blackjack
        print(' ***** Blackjack! ****** ')
    elif total > 21:
        print(' ----- Bust! ------ ')  # if the user busts

    return total  # return total


# get dealer's total from inital hand
dealers_total = total_up_hand(dealers_hand)


def game_menu():
    """ this function displays the game menu and handles user input"""
    global users_hand
    global dealers_hand
    global user_total
    global dealers_total

    while True:
        print('Your current hand : %s' % (users_hand))
        print("Dealer's hand : %s \n" % dealers_hand)
        print('1) .... Hit me ')
        print('2) .... Stay ')
        print('3) .... Exit Game')
        menu_selection = input('Select from the menu... \n')  # gets user input
        if menu_selection == '1':  # 'hit me '
            # append new card to users hand and remove it from the deck
            users_hand.append(hit_me(game_deck))
            user_total = total_up_hand(users_hand)
            if user_total > 21:  # ! if user busts
                print('You lose! ')
                tally['Losses'] += 1  # add 1 to losses
                print(tally)  # display wins/ losses/ ties
                print('\n')
                users_hand = get_cards(game_deck)  # user gets new hand
                dealers_hand = get_cards(game_deck)  # dealer gets new hand
                user_total = 0  # reset user total to 0
                dealers_total = 0  # reset dealers total to 0
        elif menu_selection == '2':  # 'stay'
            user_total = total_up_hand(users_hand)  # total up user's hand
            while dealers_total < 16:  # if user has less than 15 total points
                # get another card for dealer
                dealers_hand.append(hit_me(game_deck))
                dealers_total = total_up_hand(
                    dealers_hand)  # get dealer's new total
            if dealers_total > 21:  # ! if dealer busts
                tally['Wins'] += 1
                print('##### Dealer busts #####')
                print("##### You Win! #####")
            elif user_total > dealers_total:  # if user wins
                tally['Wins'] += 1  # add 1 to wins
                print("##### You Win! #####")
            elif user_total < dealers_total:  # if dealer wins
                tally['Losses'] += 1  # add 1 to losses
                print('##### You Lose! #####')
            else:  # if its a tie
                tally['Ties'] += 1
                print("##### Y'all Tie! #####")
            print("\nDealer's hand : %s = %d points " %
                  (dealers_hand, dealers_total))
            print("Your hand : %s = %d points" % (users_hand, user_total))
            print(tally)  # show tally of wins/losses/ties
            users_hand.clear()  # discard hand
            dealers_hand.clear()  # discard hand
            users_hand = get_cards(game_deck)  # user gets new hand
            dealers_hand = get_cards(game_deck)  # dealer gets new hand
            user_total = 0  # reset user total to 0
            dealers_total = 0  # reset dealers total to 0
            print('\n')

        else:
            print('Goodbye')
            break


game_menu()

#! to do:
#! multi-player
#! ace == 11 or 1 (now it is only 11)
#! write high score to data file
#! set max number of total losses before the game automatically quits
#! betting?
#! clean this file up by making a module for the functions
#!
