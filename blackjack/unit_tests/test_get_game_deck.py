from black_jack import User, Deck_of_cards, Cards
from collections import Counter

""" Testing Cards.get_game_deck() function that reutrns:
 a full game deck of 52 cards
 4 suites
 13 of each suite
 4 of each card (different suites)
 
     def get_game_deck(self):
        #this function builds a deck of 52 cards 
            #(4 of each suit) and returns the shuffled deck as a list
        for suit in self.suits:  # iterates through each of the suits
            for val in self.values:  # iterates through each of the values
                # appends each card to deck
                self.game_deck.append('%s of %s' % (val, suit))
        random.shuffle(self.game_deck)  # shuffles game deck
        
 
 """

def test_get_game_deck_deck_length():
    """ deck length should be 52 """
    # black_jack.py already runs the Cards.get_game_deck() function
    length = len(Cards.game_deck)
    assert length == 52

def test_get_game_deck_spades():
    """ there should be 13 spades in the deck """
    spades = 0

    for card in Cards.game_deck:
        if 'spades' in card:
            spades += 1

    assert spades == 13

def test_get_game_deck_hearts():
    """ there should be 13 hearts in the deck """
    hearts = 0

    for card in Cards.game_deck:
        if 'hearts' in card:
            hearts += 1

    assert hearts == 13

def test_get_game_deck_clubs():
    """ there should be 13 clubs in the deck """
    clubs = 0

    for card in Cards.game_deck:
        if 'clubs' in card:
            clubs += 1

    assert clubs == 13

def test_get_game_deck_diamonds():
    """ there should be 13 diamonds in the deck """
    diamonds = 0

    for card in Cards.game_deck:
        if 'clubs' in card:
            diamonds += 1

    assert diamonds == 13

def test_get_game_deck_aces():
    """ there should be 4 aces in the deck """
    aces = 0
    for card in Cards.game_deck:
        if 'Ace' in card:
            aces += 1

    assert aces == 4

def test_get_game_deck_2s():
    """ there should be 4 2s in the deck """
    two = 0
    for card in Cards.game_deck:
        if '2' in card:
            two += 1

    assert two == 4

def test_get_game_deck_3s():
    """ there should be 4 3s in the deck """
    threes = 0
    for card in Cards.game_deck:
        if '3' in card:
            threes += 1

    assert threes == 4

def test_get_game_deck_4s():
    """ there should be 4 4s in the deck """
    fours = 0
    for card in Cards.game_deck:
        if '4' in card:
            fours += 1

    assert fours == 4

def test_get_game_deck_5s():
    """ there should be 4 5s in the deck """
    fives = 0
    for card in Cards.game_deck:
        if '5' in card:
            fives += 1

    assert fives == 4

def test_get_game_deck_6s():
    """ there should be 4 6s in the deck """
    sixes = 0
    for card in Cards.game_deck:
        if '6' in card:
            sixes += 1

    assert sixes == 4

def test_get_game_deck_7s():
    """ there should be 4 7s in the deck """
    sevens = 0
    for card in Cards.game_deck:
        if '7' in card:
            sevens += 1

    assert sevens == 4

def test_get_game_deck_8s():
    """ there should be 4 8s in the deck """
    eights = 0
    for card in Cards.game_deck:
        if '8' in card:
            eights += 1

    assert eights == 4

def test_get_game_deck_9s():
    """ there should be 4 9s in the deck """
    nines = 0
    for card in Cards.game_deck:
        if '9' in card:
            nines += 1

    assert nines == 4

def test_get_game_deck_10s():
    """ there should be 4 10s in the deck """
    tens = 0
    for card in Cards.game_deck:
        if '10' in card:
            tens += 1

    assert tens == 4
def test_get_game_deck_jacks():
    """ there should be 4 jacks in the deck """
    jacks = 0
    for card in Cards.game_deck:
        if 'Jack' in card:
            jacks += 1

    assert jacks == 4

def test_get_game_deck_queens():
    """ there should be 4 queens in the deck """
    queens = 0
    for card in Cards.game_deck:
        if 'Queen' in card:
            queens += 1

    assert queens == 4

def test_get_game_deck_kings():
    """ there should be 4 kings in the deck """
    kings = 0
    for card in Cards.game_deck:
        if 'King' in card:
            kings += 1

    assert kings == 4
    
def test_get_game_deck_no_duplicates():
    """ there should be no duplicates in the game deck """
    c = Counter(Cards.game_deck)  # gets dictionary of cards and quantity for each
    duplicates = 0  # no duplicates yet
    for card in c:  # iterate through each card value pair
        if c[card] > 1:  # if there is more than 1 of any card
            duplicates += 1  # increment duplicates by 1
            
    assert duplicates == 0


