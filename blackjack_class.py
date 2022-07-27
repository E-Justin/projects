import random  # for getting a random card from an index and for shuffling 
from datetime import datetime  # for date/time
import os  # to check if file is empty or not
import pyinputplus as pyip  # for error handling


class User:
    def __init__(self, name):
        self.name = name

        self.hand = []

        self.total = 0  # total points per hand

        self.tally = {
            'Wins': 0,
            'Losses': 0,
            'Ties': 0,
        }

    def clear_hand(self):
        """ this function discards players' previous hands
            so a new game can start """
        self.hand.clear()

    def get_total(self):
        """ returns a player's total points for their hand as an int"""
        self.total = 0  # reset players total to 0 before totaling up points
        ace_counter = 0
        # tally number of aces in hand
        for card in self.hand:
            if 'Ace' in card:
                ace_counter += 1

        for card in self.hand:  # iterate through cards in hand
            if 'Ace' in card:  # if the card is an ace
                # ace == 11 (will adjust in a few lines if busts)
                self.total += 11
            elif 'Queen' in card or 'Jack' in card or 'King' in card:  # if card is a face card other than ace
                self.total += 10  # counts as 10
            else:  # if its a non face card
                # take value of card and add to total
                self.total += int(card[0:2])

        while self.total > 21 and ace_counter > 0:  # if user busts with counting ace as 11
            self.total -= 10  # make ace count as 1
            ace_counter -= 1  # decrement ace counter

    def show_hand(self):
        """ this function displays a players hand and current total"""
        print("%s's hand : %s : %d " % (self.name, self.hand, self.total))

    def handle_high_score_data(self):
        """ this function will check to see if the user got a new high score.
            if a new high score was achieved, it will write the data to a txt file
            else: it will read old high score from file """

        now = datetime.now()  # get date and time

        # open a file for reading/ writing
        f = open('blackjack_high_score.txt', 'r+')

        #! if file contains previous high score (not emtpy)
        if os.path.getsize('blackjack_high_score.txt') != 0:
            f_line = f.readline()  # read first (only) line in the file

            # this is the index in the string where the number of wins is
            x = int(f_line[7:9])

            if self.tally['Wins'] > x:  # ! if a new high score was achieved
                print('\nNew High Score of %d wins!!!' % self.tally['Wins'])
                # clear contents of file to make room for new high score
                f = open('blackjack_high_score.txt', 'w')
                # enter name to save high score
                print('%s, you are the new blackjack champion! ' % self.name)
                # write username and their high score
                f.write('Wins : %d : %s : %s' %
                        (self.tally['Wins'], self.name, now))
            else:  # ! if user did not beat old high score
                print('\nCurrent high score : ')
                print(f_line)
                print('Better luck next time. ')

        elif self.tally['Wins'] > 0:  # if file is empty and the user got 1 or more wins
            print('\nNew (1st) High Score of %d wins!!!' % self.tally['Wins'])
            # enter name to save high score
            print('%s, you are the new blackjack champion! ' % self.name)
            # write username and their high score
            # write high score to file
            f.write('Wins : %d : %s : %s' %
                    (self.tally['Wins'], self.name, now))
        else:
            print('\nBetter luck next time. ')

        f.close()  # close file when done


class Deck_of_cards:
    def __init__(self):
        self.suits = ['spades', 'hearts', 'diamonds', 'clubs']

        self.values = [2, 3, 4, 5, 6, 7, 8,
                       9, 10, 'Jack', 'Queen', 'King', 'Ace']

        self.game_deck = []

    def get_game_deck(self):
        """this function builds a deck of 52 cards 
            (4 of each suit) and returns the shuffled deck as a list"""
        for suit in self.suits:  # iterates through each of the suits
            for val in self.values:  # iterates through each of the values
                # appends each card to deck
                self.game_deck.append('%s of %s' % (val, suit))
        random.shuffle(self.game_deck)  # shuffles game deck

    def get_cards(self):
        """ this function deals / returns two random cards
            to player  (also removes the cards dealt from the game deck) """
        hand = []
        for i in range(2):  # 2 cards
            # randomly gets a card's index
            card_index = random.randint(0, (len(self.game_deck) - 1))
            # gets the card from random index
            card = self.game_deck[card_index]
            hand.append(card)  # appends to user's hand
            self.game_deck.remove(card)  # removes card from game deck
        return hand

    def hit_me(self, person):
        """ this function deals one random card to player
            and removes it from the game deck"""
        length = len(
            self.game_deck)  # get length (it changes when a card is dealt)

        # randomly get next card's index
        card_index = random.randint(0, (length - 1))
        card = self.game_deck[card_index]  # get random card
        person.hand.append(card)  # append new card to dealers hand
        self.game_deck.remove(card)  # remove card from deck


Cards = Deck_of_cards()  # instantiate class instance

Cards.get_game_deck()  # get shuffled deck of 52 cards

# get player1's name
name = input('Welcome to Blackjack, please enter your name ... ')

Player1 = User(name)  # intantiate class instance
print('Welcome %s ' % Player1.name)
Dealer = User('Dealer')  # intantiate class instance


def game_menu():
    round_number = 0  # to keep track of how many games have been played
    while True:
        round_number += 1
        if round_number > 1:  # !  if this is not the first game
            print(Player1.tally)  # display wins/losses/ties
        if round_number == 1:  # ! if it is game number 1
            print('1) ... Play Blackjack ')
        elif round_number > 1:  # ! if it is not game 1
            print('1) ... Play again ')
        print('2) ... Exit Game ')
        selection = pyip.inputInt(
            'Choose from the menu ... ')  # get user selection
        if selection != 1 and selection != 2:  # ! if selection was not a valid choice
            print('\n*** Invalid selection ***\n')
        elif selection == 2:  # ! if user selects to exit game
            if round_number > 1:
                # check to see if new high score / show old high score
                Player1.handle_high_score_data()
            print('Goodbye')
            break
        else:  # ! if user chooses to play
            Player1.clear_hand()  # discard players' hands so a new game can start
            Dealer.clear_hand()

            Cards.get_game_deck()  # get game_deck

            # deal 2 random cards to player1 and remove them from game deck
            Player1.hand = Cards.get_cards()
            # deal 2 random cards to dealer and remove them from game deck
            Dealer.hand = Cards.get_cards()

            while True:
                print('\n')
                #  calculate totals
                Player1.get_total()  # get user total
                Dealer.get_total()  # get dealer total

                #  display hands and totals
                print('\n')
                Player1.show_hand()
                Dealer.show_hand()
                print('\n')

                #! ~~~~~~~~~~~~~~~ conditional statements to handle blackjacks or busting  ~~~~~~~~~~~~~~~
                if Player1.total == 21 and len(Player1.hand) == 2:
                    # ! if both got blackjack
                    if Dealer.total == 21 and len(Dealer.hand) == 2:
                        print('### Yall both got blackjack ###\n')
                        Player1.tally['Ties'] += 1  # add 1 to ties
                        break
                    else:  # ! if user got blackjack
                        print('Player 1 got Blackjack!\n')
                        Player1.tally['Wins'] += 1  # add 1 to wins
                        break
                # ! if dealer got blackjack
                elif Dealer.total == 21 and len(Dealer.hand) == 2:
                    print('Dealer got Blackjack!\n')
                    Player1.tally['Losses'] += 1  # add 1 to losses
                    break
                elif Player1.total > 21:  # ! if user busted
                    print('Player 1 busted!\n')
                    Player1.tally['Losses'] += 1  # add 1 to losses
                    break
                elif Dealer.total > 21:  # ! if dealer busted
                    print('Dealer busted! \n')
                    Player1.tally['Wins'] += 1  # add 1 to wins
                    break

                #!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #  display wins/ losses/ ties
                print(Player1.tally)
                print('1) ... Hit me! ')
                print('2) ... Stay')
                print('3) ... Exit Game')
                selection = pyip.inputInt(
                    'Choose from the menu ...')  # get user input
                if selection != 1 and selection != 2 and selection != 3:  # ! if user selects an invalid choice
                    print('\n*** Invalid selection ***\n')
                elif selection == 1:  # ! hit me
                    Cards.hit_me(Player1)  # deal 1 new card to player 1
                elif selection == 2:  # ! stay
                    while Dealer.total <= 17:  # while dealer has a total less than or equal to 17
                        Cards.hit_me(Dealer)  # dealer gets another card
                        Dealer.get_total()  # calculate dealer's new total

                    Player1.show_hand()  # show player1's hand
                    Dealer.show_hand()  # show dealer's hand

                    if Dealer.total > 21:  # ! if dealer busted
                        print('\nDealer busted! \n')
                        Player1.tally['Wins'] += 1  # add 1 to wins
                        break
                    elif Player1.total > Dealer.total:  # ! if user wins
                        print('\nPlayer 1 wins! \n')
                        Player1.tally['Wins'] += 1  # add 1 to wins
                        break
                    elif Player1.total < Dealer.total:  # ! if dealer wins
                        print('\nDealer wins! \n')
                        Player1.tally['Losses'] += 1  # add 1 to losses
                        break
                    else:  # ! if players tied
                        print("\nY'all tied! \n")
                        Player1.tally['Ties'] += 1  # add 1 to ties
                        break
                else:  # ! exit game
                    # check to see if new high score/ show old high score
                    Player1.handle_high_score_data()
                    print('Goodbye ...')
                    return


game_menu()
