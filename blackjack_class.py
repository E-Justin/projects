import random


class Card_handler:
    def __init__(self):
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

        return total


Cards = Card_handler()  # instantiate Cards class


game_over = False

while game_over is False:
    print('1) ... Play Blackjack ')
    print('2) ... Exit Game ')
    selection = input('Choose from the menu ... ')  # get user selection
    if selection != '1' and selection != '2':  # if selection was not a valid choice
        print('\n*** Invalid selection ***\n')
    elif selection == '2':  # if user selects to exit game
        print('Goodbye')
        break
    else:  # if user chooses to play
        Cards.get_game_deck()  # get game_deck

        Cards.get_cards()  # deals cards to player1 and dealer

        # display each player's hand
        print('\n')
        print("Player 1's hand : %s" % Cards.users_hand)
        print("Dealer's hand   : %s\n" % Cards.dealers_hand)
        Cards.get_users_total()
