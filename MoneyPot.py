

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
