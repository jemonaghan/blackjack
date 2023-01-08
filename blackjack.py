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

class MoneyPot:

    def __init__(self):
        self.amount = 100
        self.bet = 0
        
    def place_bet(self):

        while True:
            try:
                print("How much would you like to bet? You have £{}\n".format(self.amount))
                self.bet = int(input("£"))
            except ValueError:
                print("Sorry the value needs to be a whole number")
            else:
                if self.bet > self.amount:
                    print("Sorry your bet can't exceed what's in your pot, you have £{}".format(self.amount))
                else:
                    break
                
    
    def calculate_winnings(self, winner):
        
        if "player has won" in winner.lower() or "player wins" in winner.lower():
            self.amount += 2*self.bet
        elif "draw" in winner.lower():
            pass
        else:
            self.amount -= self.bet
        print("You have £{} in your pot".format(self.amount))

    def can_play(self):
        return self.amount >0

        


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

    x = input("\nWould you like to hit or stand? Enter 'h' or 's'\n")
    if x[0].lower() == 'h':    
        return False
    elif x[0].lower() == 's':
        return True
    else:
        print("\nError, please try again! Enter 'h' or 's'\n")
        return player_hit_or_stand(total)

#dealer/automatic strategy: hit or stand
def dealer_hit_or_stand(total):
    return total >= 17

# winner calculation
def calculate_winner(user_total, dealer_total):
   
    if user_total >21:
        return "\nThe player is bust! Dealer wins\n"
    if dealer_total >21:
        return "\nThe dealer is bust! Player wins!\n"
    if user_total == dealer_total:
        return "\nIt's a draw!\n"
    if user_total == 21 and dealer_total != 21:
        return "\nThe player has won!\n"
    if dealer_total == 21 and user_total != 21:
        return "\nThe dealer has won!\n"
    if user_total > dealer_total:
        return  "\nThe player has won!\n"
    return  "\nThe dealer has won!\n"

def print_winner(user_total, dealer_total):
    print("\nThe player total is {}".format(user_total))
    print("The dealer total is {}".format(dealer_total))
    winner = calculate_winner(user_total, dealer_total)
    print(winner)
    return winner

def game(deck, hit_or_stand_fn):

    hand = deck.start_game()
    hand_total = total(hand)

    print("\nStarting hand:\n {}".format(hand))

    stand = False

    while stand == False:
        stand = hit_or_stand_fn(hand_total)
        if not stand:
            deck.deal(hand)
            print("\nNew hand is:\n {}".format(hand))
            hand_total = total(hand)
      
    return hand_total

def choose_to_play(money_pot):
    if not money_pot.can_play():
        return print("Sorry you've run out of cash, Better luck next time!")
        
    new_hand = input("\nWould you like to play another hand of Blackjack? Enter 'y' or 'n'\n")
    if new_hand[0].lower() == 'y': 
        blackjack_game(money_pot)
    elif new_hand[0].lower() == 'n':
        print("Thanks for playing!")
    else:
        print("\nError, please try again! Enter 'y' or 'n'\n")
        return choose_to_play(money_pot)

def blackjack_game(money_pot):
    money_pot.place_bet()
    deck = Deck()
    user_total = game(deck, player_hit_or_stand)
    dealer_total = game(deck, dealer_hit_or_stand)
    winner = print_winner(user_total, dealer_total)
    money_pot.calculate_winnings(winner)
    choose_to_play(money_pot)
    
   

if __name__ == '__main__':
    print("\n\nwelcome to Blackjack! Can you beat the dealer and get to 21 without going bust?\n")
    blackjack_game(MoneyPot()) 
        

    



        



