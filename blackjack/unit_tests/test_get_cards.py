from black_jack import Player1, Cards, Dealer

""" Testing get_cards() function
    this function deals/ returns two random cards to a player 
    and removes them from the game deck 
    """

def test_get_cards_to_one_player_length_of_game_deck_should_decrease_by_two():
    # game deck starts off with 52 cards
    Dealer.hand = Cards.get_cards()  # deal 2 cards to dealer
    assert len(Cards.game_deck) == 50

def test_get_cards_to_two_players_length_of_game_deck_should_decrease_by_four():
    # game deck starts off with 52 cards
    Dealer.hand = Cards.get_cards()  # deal 2 cards to dealer
    Player1.hand = Cards.get_cards()  # deal 2 cards to player1
    assert len(Cards.game_deck) == 48

def test_get_cards_player_hand_should_have_length_of_two():
    Player1.hand = Cards.get_cards()  # deal 2 cards to player1
    assert len(Player1.hand) == 2

