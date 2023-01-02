from src.deck import Deck
import random


#def play():
#   print('Hello, potential future BBC developer!')  # execution starts here! delete this line and add your game code.


#create deck and shuffle it for a game

def create_deck():
    value = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King", "Ace"]
    suits = ["Spades","Hearts","Clubs","Diamonds"]

    deck = []
    for s in suits:
        for v in value:
            deck.append((v,s))
    
    random.shuffle(deck)
    return deck
  
#deals first hand with two cards
def start_game():
    hand = []
    for i in range(2):
       hand = deal(hand)
    return hand

#deals a single card to players hand. If its an Ace it will go to the end of the hand to be counted last
def deal(hand):
    card = deck.pop()
    if card [0] == "Ace":
        hand.append(card)
    else:
        hand.insert(0, card)
    return hand


#calculates total in hand
def total(hand):
    total = 0
    for card in hand: 
        total += get_value(card, total)
    return total


#gets value of card to calculate totals. Ace checked last as appended to hand 
def get_value(card, total):
    value = card [0]   
    if type(value) == int: return value
    if value != "Ace": return 10
    if total <= 10: return 11
    return 1


#player chooses to hit or stand
def hit_or_stand():
    x = input ("Would you like to hit or stand?Enter 'h' or 's'")
    if x[0].lower() == 'h':    
        return False
    elif x[0].lower() == 's':
        return True
    else:
        print("Error, please try again")
        return hit_or_stand()


#print score or if its a win/loss
def calculate_win(user_total, dealer_total):
    print("The player total is {}".format(user_total))
    print("The dealer total is {}".format(dealer_total))
    if user_total >21:
        print("The player is bust! Dealer wins")
    if dealer_total >21 and user_total <=21:
        print("The dealer is bust! Player wins!")    
    if user_total == dealer_total:
        print("It's a draw!")
    if user_total == 21 and dealer_total != 21:
        print("Blackjack! The player has won!")
    if dealer_total == 21 and user_total != 21:
        print("Blackjack! The dealer has won!")
    if user_total > dealer_total:
        print( "The player wins!")
    if dealer_total > user_total:
        print( "The dealer wins!")


deck = create_deck()   

def game():

    

    hand = start_game()
    #hand = deal(hand)

    hand_total = total(hand)

    print(hand)

    #hand_total = get_result(hand_total)
    stand = False



    while hand_total < 21 and stand == False:
        stand = hit_or_stand()
        if not stand:
            deal(hand)
            print(hand)
            hand_total = total(hand)
    
    
    return hand_total
    #calculate_win(hand_total)


user_total = game()


dealer_total = game()
calculate_win(user_total, dealer_total)
#print(hand)
#print(hand_total)
#print(hand_result)

#input players
#compare result for winner

#if __name__ == '__main__':
#play()
