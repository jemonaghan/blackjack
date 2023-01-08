import unittest
from src.blackjack import dealer_hit_or_stand, calculate_winner, game
from src.Deck import Deck
from src.MoneyPot import MoneyPot


class BlackjackTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

#test 21 is calculated with two cards

    def test_dealer_gets_21_with_two_cards(self):
        spec_deck = Deck()
        spec_deck.cards = [('Ace', 'Diamonds'), ('Jack', 'Hearts')]
        my_result = game(spec_deck, dealer_hit_or_stand)
        self.assertEqual(my_result, 21)

#test Ace counted as 1 and last. Hits on 16

    def test_ace_counted_as_1_and_last(self):
        spec_deck = Deck()
        spec_deck.cards = [(5, 'Diamonds'), (10, 'Diamonds'), (5, 'Spades'), ('Ace', 'Clubs')]
        my_result = game(spec_deck, dealer_hit_or_stand)
        self.assertEqual(my_result, 21)

#test Ace counted as 11. (stands after two cards)

    def test_ace_counted_as_11_and_last(self):
        spec_deck = Deck()
        spec_deck.cards = [(5, 'Diamonds'),('Jack', 'Spades'), ('Ace', 'Hearts')]
        my_result = game(spec_deck, dealer_hit_or_stand)
        self.assertEqual(my_result, 21)


#test dealer stands on 17
    def test_dealer_stands_on_17(self):
        spec_deck = Deck()
        spec_deck.cards = [(4, 'Diamonds'), ('Jack', 'Hearts'), (7, 'Hearts')]
        my_result = game(spec_deck, dealer_hit_or_stand)
        self.assertEqual(my_result, 17)


#test dealer hits when hand is <17
    def test_dealer_hits_when_less_than_17(self):
        spec_deck = Deck()
        spec_deck.cards = [(4, 'Diamonds'), ('Jack', 'Hearts'), (6, 'Hearts')]
        my_result = game(spec_deck, dealer_hit_or_stand)
        self.assertEqual(my_result, 20)

#test dealer goes bust 
    def test_dealer_goes_bust(self):
        spec_deck = Deck()
        spec_deck.cards = [('King', 'Diamonds'), ('Jack', 'Hearts'), (6, 'Hearts')]
        my_result = game(spec_deck, dealer_hit_or_stand)
        self.assertEqual(my_result, 26)

#test deal function deals one card
    def test_deck_deals_card(self):
        spec_deck = Deck()
        spec_deck.cards = [('King', 'Diamonds'), ('Jack', 'Hearts'), (6, 'Hearts')]
        my_hand = spec_deck.deal([])
        self.assertEqual(my_hand, [(6, 'Hearts')])

#test starting hand has two card    
    def test_starting_hand_has_two_cards(self):
        spec_deck = Deck()
        spec_deck.cards = [('King', 'Diamonds'), ('Jack', 'Hearts'), (6, 'Hearts')]
        my_hand = spec_deck.start_game()
        self.assertEqual(my_hand, [('Jack', 'Hearts'),(6 ,'Hearts')])

#test deck starts with 52 cards
    def test_initial_deck_size_is_52(self):
        deck_size = len(self.deck.cards)
        self.assertEqual(deck_size, 52)

#calculate winner function tests
    
    def test_calculate_dealer_winner_if_player_bust(self):
        self.assertIn("The player is bust", calculate_winner (22, 18)) #"The player is bust! Dealer wins"
        self.assertIn("Dealer wins", calculate_winner (22, 18))
    
    def test_calculate_player_winner_if_dealer_bust(self):
        self.assertIn("Player wins", calculate_winner (18, 22)) #"The dealer is bust! Player wins!")
        self.assertIn("The dealer is bust", calculate_winner (18, 22))

    def test_calculate_draw_if_user_and_player_total_equal(self):
        self.assertIn("It's a draw", calculate_winner (18, 18)) #"It's a draw!"
    
    def test_calculate_player_wins_with_21_dealer_not_21(self):
        self.assertIn("The player has won", calculate_winner (21, 18)) #"The player has won!"
    
    def test_dealer_wins_with_21_player_not_21(self):
        self.assertIn("The dealer has won", calculate_winner (18, 21))#"The dealer has won!"

    def test_calculate_player_wins_with_highest_total(self):
        self.assertIn("The player has won", calculate_winner (20, 18))#"The player has won!"

    def test_dealer_wins_with_highest_total(self):
        self.assertIn("The dealer has won", calculate_winner (18, 20))#"The dealer has won!"
    
    def test_dealer_wins_if_both_bust(self):
        self.assertIn("Dealer wins", calculate_winner (22, 22)) #"The player is bust! Dealer wins"

#test calculate money pot. Default moneypot is 100
#test when the player wins, the bet gets doubled and added to moneypot
    def test_player_wins_bet_doubles_adds_to_moneypot(self):
        spec_moneypot = MoneyPot()
        spec_moneypot.bet = 20
        spec_moneypot.calculate_winnings('player has won')
        self.assertEqual(spec_moneypot.amount, 140)
        
#test when the dealer/player draws, the bet stays in the moneypot
    def test_draw_moneypot_maintained(self):
        spec_moneypot = MoneyPot()
        spec_moneypot.bet = 20
        spec_moneypot.calculate_winnings('draw')
        self.assertEqual(spec_moneypot.amount, 100)

#test when the dealer wins, the bet is deducted from the moneypot
    def test_dealer_wins_bet_subtracted_from_moneypot(self):
        spec_moneypot = MoneyPot()
        spec_moneypot.bet = 20
        spec_moneypot.calculate_winnings('The dealer has won')
        self.assertEqual(spec_moneypot.amount, 80)

#test when moneypot is at 0, the game ends and cannot choose to play
    def test_not_able_to_play_if_moneypot_0(self):
        spec_moneypot = MoneyPot()
        spec_moneypot.amount = 0
        self.assertFalse(spec_moneypot.can_play())

#test when moneypot is above 0, player can choose to play

    def test_can_play_if_moneypot_positive(self):
        spec_moneypot = MoneyPot()
        self.assertTrue(spec_moneypot.can_play())


if __name__ == '__main__':
    unittest.main()


""" 
Given I play a game of blackjack
When I am dealt my opening hand
Then I have two cards

def test_opening_hand_is_two(self):
    self.assertEqual(opening_hand, 2)

test hand calculation
with A/K/Q/J

Given I have a valid hand of cards
When I choose to ‘hit’
Then I receive another card
And my score is updated

Given I have a valid hand of cards
When I choose to ‘stand’
Then I receive no further cards
And my score is evaluated

Given my score is updated or evaluated
When it is 21 or less
Then I have a valid hand

def test_valid_hand_<21(self):
    self.assertTrue(valid_hand, 20)

def test_valid_hand_=21(self):
    self.assertTrue(valid_hand, 21)

Given my score is updated
When it is 22 or more 
Then I am ‘bust’ and do not have a valid hand

def test_valid_hand_false_=>22(self)
    self.assertFalse(valid_hand, 22)

Given I have a king and an ace
When my score is evaluated
Then my score is 21

Given I have a king, a queen, and an ace
When my score is evaluated
Then my score is 21

Given that I have a nine, an ace, and another ace
When my score is evaluated
Then my score is 21	

suit = 13cards
52cards
"""

