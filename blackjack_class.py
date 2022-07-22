import random


class Game_manager:
    def __init__(self):
        self.tally = {
            'Wins': 0,
            'Losses': 0,
            'Ties': 0,
        }

        self.game_deck = []

        self.users_hand = []
        self.dealers_hand = []

        self.users_total = 0
        self.dealers_total = 0

        self.suits = ['spades', 'hearts', 'diamonds', 'clubs']

        self.values = [2, 3, 4, 5, 6, 7, 8,
                       9, 10, 'Jack', 'Queen', 'King', 'Ace']

    def get_game_deck(self):
        """this function builds a deck of 52 cards 
            (4 of each suit) and returns the shuffled deck as a list"""
        for suit in self.suits:  # iterates through each of the suits
            for val in self.values:  # iterates through each of the values
                # appends each card to deck
                self.game_deck.append('%s of %s' % (val, suit))
        random.shuffle(self.game_deck)  # shuffles game deck

    def get_cards(self):
        """ this function deals two random cards
            to the dealer and player 1 (also removes
            the cards dealt from the game deck) """

        for i in range(2):  # 2 cards
            # randomly gets a card's index
            card_index = random.randint(0, (len(self.game_deck) - 1))
            # gets the card from random index
            card = self.game_deck[card_index]
            self.users_hand.append(card)  # appends to user's hand
            self.game_deck.remove(card)  # removes card from game deck
        for i in range(2):  # 2 cards
            # randomly gets a card's index
            card_index = random.randint(0, (len(self.game_deck) - 1))
            # gets the card from random index
            card = self.game_deck[card_index]
            self.dealers_hand.append(card)  # appends to dealer's hand
            self.game_deck.remove(card)  # removed card from game deck

    def get_users_total(self):
        """ returns user's total points for their hand as an int"""
        ace_counter = 0
        # tally number of aces in hand
        for card in self.users_hand:
            if 'Ace' in card:
                ace_counter += 1

        total = 0

        for card in self.users_hand:  # iterate through cards in hand
            if 'Ace' in card:  # if the card is an ace
                total += 11  # ace == 11 (will adjust in a few lines if busts)
            elif 'Queen' in card or 'Jack' in card or 'King' in card:  # if card is a face card other than ace
                total += 10  # counts as 10
            else:  # if its a non face card
                total += int(card[0:2])  # take value of card and add to total

        while total > 21 and ace_counter > 0:  # if user busts with counting ace as 11
            total -= 10  # make ace count as 1
            ace_counter -= 1  # decrement ace counter

        self.users_total = total

    def get_dealers_total(self):
        """ returns user's total points for their hand as an int"""
        ace_counter = 0
        # tally number of aces in hand
        for card in self.dealers_hand:
            if 'Ace' in card:
                ace_counter += 1

        total = 0

        for card in self.dealers_hand:  # iterate through cards in hand
            if 'Ace' in card:  # if the card is an ace
                total += 11  # ace == 11 (will adjust in a few lines if busts)
            elif 'Queen' in card or 'Jack' in card or 'King' in card:  # if card is a face card other than ace
                total += 10  # counts as 10
            else:  # if its a non face card
                total += int(card[0:2])  # take value of card and add to total

        while total > 21 and ace_counter > 0:  # if user busts with counting ace as 11
            total -= 10  # make ace count as 1
            ace_counter -= 1  # decrement ace counter

        self.dealers_total = total

    def dealer_says_hit_me(self):
        """ this function deals one random card to dealer 
            and removes it from the game deck """
        length = len(
            self.game_deck)  # get length (it changes when a card is dealt)

        # randomly get next card's index
        card_index = random.randint(0, (length - 1))
        card = self.game_deck[card_index]  # get random card
        self.dealers_hand.append(card)  # append new card to dealers hand
        self.game_deck.remove(card)  # remove card from deck

    def user_says_hit_me(self):
        """ this function deals one random card to user
            and removes it from the game deck"""
        length = len(
            self.game_deck)  # get length (it changes when a card is dealt)

        # randomly get next card's index
        card_index = random.randint(0, (length - 1))
        card = self.game_deck[card_index]  # get random card
        self.users_hand.append(card)  # append new card to dealers hand
        self.game_deck.remove(card)  # remove card from deck

    def clear_hands(self):
        """ this function discards players' previous hands
            so a new game can start """
        self.users_hand.clear()
        self.dealers_hand.clear()


Cards = Game_manager()  # instantiate Cards class


def game_menu():
    while True:
        print('1) ... Play Blackjack ')
        print('2) ... Exit Game ')
        selection = input('Choose from the menu ... ')  # get user selection
        if selection != '1' and selection != '2':  # ! if selection was not a valid choice
            print('\n*** Invalid selection ***\n')
        elif selection == '2':  # ! if user selects to exit game
            print('Goodbye')
            break
        else:  # ! if user chooses to play
            Cards.clear_hands()

            Cards.get_game_deck()  # get game_deck

            Cards.get_cards()  # deals cards to player1 and dealer

            while True:
                print('\n')
                #  calculate totals
                Cards.get_users_total()  # get user total
                Cards.get_dealers_total()  # get dealer total

                #  display hands and totals
                print("Player 1's hand : %s : %d" %
                      (Cards.users_hand, Cards.users_total))
                print("Dealer's hand   : %s : %d\n" %
                      (Cards.dealers_hand, Cards.dealers_total))

                #! ~~~~~~~~~~~~~~~ conditional statements to handle blackjacks or busting  ~~~~~~~~~~~~~~~
                if Cards.users_total == 21 and len(Cards.users_hand) == 2:
                    # ! if both got blackjack
                    if Cards.dealers_total == 21 and len(Cards.dealers_hand) == 2:
                        print('### Yall both got blackjack ###\n')
                        Cards.tally['Ties'] += 1  # tied
                        break
                    else:  # ! if user got blackjack
                        print('Player 1 got Blackjack!\n')
                        Cards.tally['Wins'] += 1  # win
                        break
                # ! if dealer got blackjack
                elif Cards.dealers_total == 21 and len(Cards.dealers_hand) == 2:
                    print('Dealer got Blackjack!\n')
                    Cards.tally['Losses'] += 1  # lose
                    break
                elif Cards.users_total > 21:  # ! if user busted
                    print('Player 1 busted!\n')
                    Cards.tally['Losses'] += 1  # lose
                    break
                elif Cards.dealers_total > 21:  # ! if dealer busted
                    print('Dealer busted! \n')
                    Cards.tally['Wins'] += 1  # win
                    break

                #!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                #  display wins/ losses/ ties
                print(Cards.tally)
                print('1) ... Hit me! ')
                print('2) ... Stay')
                print('3) ... Exit Game')
                selection = input('Choose from the menu ...')  # get user input
                if selection != '1' and selection != '2' and selection != '3':  # if user selects an invalid choice
                    print('\n*** Invalid selection ***\n')
                elif selection == '1':  # hit me
                    Cards.user_says_hit_me()
                else:  # stay
                    print('Goodbye ...')
                    return


game_menu()

""" 
Todo:
1. decide who wins after user chooses to stay
2. dealer continues getting another card after user stays until total is at or above 17
2. betting
3. write high score to file

"""
