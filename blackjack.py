# from src.deck import Deck
import random


#create deck and shuffle it for a game
class Deck:
    def __init__(self):
        self.create_deck()

    def create_deck(self):
        value = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King", "Ace"]
        suits = ["Spades","Hearts","Clubs","Diamonds"]

        self.cards = []
        for s in suits:
            for v in value:
                self.cards.append((v,s))
        
        random.shuffle(self.cards)

        

    
    #deals a single card to players hand. If its an Ace it will go to the end of the hand to be counted last
    def deal(self, hand):
        card = self.cards.pop()
        if card [0] == "Ace":
            hand.append(card)
        else:
            hand.insert(0, card)
        return hand
    
    #deals first hand with two cards
    def start_game(self):
        hand = []
        for i in range(2):
            hand = self.deal(hand)
        return hand



#calculates total in hand
def total(hand):
    total = 0
    for card in hand: 
        total += get_value(card, total)
    return total


#gets value of card to calculate totals. Ace checked last
def get_value(card, total):
    value = card [0]   
    if type(value) == int: return value
    if value != "Ace": return 10
    if total <= 10: return 11
    return 1


#player/manual strategy: hit or stand
def player_hit_or_stand(total):
    if total >=21:
        return True

    x = input ("Would you like to hit or stand?Enter 'h' or 's'")
    if x[0].lower() == 'h':    
        return False
    elif x[0].lower() == 's':
        return True
    else:
        print("Error, please try again")
        return player_hit_or_stand()

#dealer/automatic strategy: hit or stand
def dealer_hit_or_stand(total):
    return total >= 17

# winner calculation
def calculate_winner(user_total, dealer_total):
   
    if user_total >21:
        return "The player is bust! Dealer wins"
    if dealer_total >21:
        return "The dealer is bust! Player wins!"
    if user_total == dealer_total:
        return "It's a draw!"
    if user_total == 21 and dealer_total != 21:
        return "The player has won!"
    if dealer_total == 21 and user_total != 21:
        return "The dealer has won!"
    if user_total > dealer_total:
        return  "The player has won!"
    return  "The dealer has won!"

def print_winner(user_total, dealer_total):
    print("The player total is {}".format(user_total))
    print("The dealer total is {}".format(dealer_total))
    print(calculate_winner(user_total, dealer_total))

def game(deck, hit_or_stand_fn):

    hand = deck.start_game()
    hand_total = total(hand)

    print(hand)

    stand = False

    while stand == False:
        stand = hit_or_stand_fn(hand_total)
        if not stand:
            deck.deal(hand)
            print(hand)
            hand_total = total(hand)
      
    return hand_total


if __name__ == '__main__':

    deck = Deck()
    user_total = game(deck, player_hit_or_stand)
    dealer_total = game(deck, dealer_hit_or_stand)
    print_winner(user_total, dealer_total)

