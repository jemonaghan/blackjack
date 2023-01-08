
from Deck import Deck
from MoneyPot import MoneyPot



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
        return print("Sorry you've run out of cash, Better luck next time!\n")

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
        

    



        



