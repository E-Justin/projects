from black_jack import Player1, Cards, Dealer

""" Testing hit_me()
    this function deals a random card from the game deck to a player
    and removes it from the game deck """

def test_hit_me_twice_player_should_have_four_cards():
    Dealer.hand = ['Ace of spades', 'Jack of hearts']
    Cards.hit_me(Dealer)  # get one more card
    Cards.hit_me(Dealer)  # get one more card

    assert len(Dealer.hand) == 4

def test_hit_me_three_times_player_should_have_five_cards():
    Dealer.hand = ['Ace of spades', 'Jack of hearts']
    Cards.hit_me(Dealer)  # get one more card
    Cards.hit_me(Dealer)  # get one more card
    Cards.hit_me(Dealer)  # get one more card

    assert len(Dealer.hand) == 5

def test_hit_me_four_times_player_should_have_six_cards():
    Dealer.hand = ['Ace of spades', 'Jack of hearts']
    Cards.hit_me(Dealer)  # get one more card
    Cards.hit_me(Dealer)  # get one more card
    Cards.hit_me(Dealer)  # get one more card
    Cards.hit_me(Dealer)  # get one more card

    assert len(Dealer.hand) == 6

def test_hit_me_once_length_of_game_deck_should_decrease_by_one():
    Dealer.hand = Cards.get_cards()  # get first two cards
    Cards.hit_me(Dealer)  # get one more card

    assert len(Cards.game_deck) == 49  # 52 - 3 == 49

def test_hit_me_twice_length_of_game_deck_should_decrease_by_two():
    Dealer.hand = Cards.get_cards()  # get first two cards
    Cards.hit_me(Dealer)  # get one more card
    Cards.hit_me(Dealer)  # get one more card

    assert len(Cards.game_deck) == 48  # 52 - 4 == 48

def test_hit_me_three_times_length_of_game_deck_should_decrease_by_three():
    Dealer.hand = Cards.get_cards()  # get first two cards
    Cards.hit_me(Dealer)  # get one more card
    Cards.hit_me(Dealer)  # get one more card
    Cards.hit_me(Dealer)  # get one more card

    assert len(Cards.game_deck) == 47  # 52 - 5 == 47

def test_hit_me_no_duplicates():
    Dealer.hand = Cards.get_cards()  # get first two cards
    Cards.hit_me(Dealer)  # get one more card

    duplicates = False  # no duplicates yet

    for card in Dealer.hand:  # iterate through cards in dealer's hand
        if card in Cards.game_deck:  # if a duplicate is found
            duplicates = True

    assert duplicates is False

def test_hit_me_twice_no_duplicates():
    Dealer.hand = Cards.get_cards()  # get first two cards
    Cards.hit_me(Dealer)  # get one more card
    Cards.hit_me(Dealer)  # get one more card

    duplicates = False  # no duplicates yet

    for card in Dealer.hand:  # iterate through cards in dealer's hand
        if card in Cards.game_deck:  # if a duplicate is found
            duplicates = True

    assert duplicates is False

def test_hit_me_when_player_has_two_cards_gets_a_third():
    Dealer.hand = ['Ace of spades', 'Jack of hearts']
    Cards.hit_me(Dealer)  # Get one more card

    assert len(Dealer.hand) == 3

def test_hit_me_when_player_has_three_cards_gets_a_fourth():
    Dealer.hand = ['Ace of spades', 'Jack of hearts', 'Queen of diamonds']
    Cards.hit_me(Dealer)  # Get one more card

    assert len(Dealer.hand) == 4

