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