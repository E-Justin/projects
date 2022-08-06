""" Testing the Dealer.get_total() function that returns the player's total points for their current hand

        def get_total(self):
         # returns a player's total points for their hand as an int
        self.total = 0  # reset players total to 0 before totaling up points
        ace_counter = 0  # tally number of aces in hand
        for card in self.hand:  # iterate through each card in hand
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

        return self.total
"""

from black_jack import User, Dealer


def test_get_total_with_blackjack():
    Dealer.hand = ['Ace of hearts', 'Jack of clubs']
    assert Dealer.get_total() == 21

def test_get_total_with_two_aces_and_adjusting_score_3_cards_total():
    Dealer.hand = ['Ace of clubs', 'Ace of hearts', '8 of diamonds']
    assert Dealer.get_total() == 20

def test_get_total_with_one_ace_and_adjusting_score_3_cards_total():
    Dealer.hand = ['Ace of clubs', 'Jack of hearts', '10 of spades']
    assert Dealer.get_total() == 21

def test_get_total_with_two_aces_and_adjusting_score_5_cards_total():
    Dealer.hand = ['Ace of clubs', 'Ace of hearts', '3 of diamonds', '5 of spades', '6 of hearts']
    assert Dealer.get_total() == 16

def test_get_total_with_bust_3_cards_total():
    Dealer.hand = ['King of spades', '10 of hearts', '7 of clubs']
    assert Dealer.get_total() == 27

def test_get_total_with_bust_5_cards_total():
    Dealer.hand = ['2 of spades', '4 of hearts', '8 of clubs', '9 of hearts', 'Queen of diamonds']
    assert Dealer.get_total() == 33

def test_get_total_with_only_two_aces():
    Dealer.hand = ['Ace of clubs', 'Ace of hearts']
    assert Dealer.get_total() == 12

def test_get_total_with_only_two_sixes():
    Dealer.hand = ['6 of hearts', '6 of clubs']
    assert Dealer.get_total() == 12

