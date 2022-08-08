from black_jack import User, Deck_of_cards, Cards, Dealer

""" Testing clear_hand() function that empties user hand. 
    after running the function, they should have no cards left in their hand """

def test_clear_hand_with_two_cards():
    Dealer.hand = ['Ace of spades', 'Jack of clubs']

    Dealer.clear_hand()

    assert Dealer.hand == []

def test_clear_hand_with_three_cards():
    Dealer.hand = ['10 of hearts', '4 of clubs', '3 of diamonds']

    Dealer.clear_hand()

    assert Dealer.hand == []

def test_clear_hand_with_four_cards():
    Dealer.hand = ['10 of hearts', '4 of clubs', '3 of diamonds', 'Ace of spades']

    Dealer.clear_hand()

    assert Dealer.hand == []

def test_clear_hand_with_five_cards():
    Dealer.hand = ['10 of hearts', '4 of clubs', '3 of diamonds', 'Ace of spades', 'Jack of clubs']

    Dealer.clear_hand()

    assert Dealer.hand == []

def test_clear_hand_with_six_cards():
    Dealer.hand = ['10 of hearts', '4 of clubs', '3 of diamonds', 'Ace of spades', 'Jack of clubs', '7 of spades']

    Dealer.clear_hand()

    assert Dealer.hand == []


