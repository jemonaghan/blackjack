# Blackjack Tech Test 

This is a console based blackjack game written in Python!

Can you get to 21 and beat the dealer? Place your bets! Win the hand you'll double your money! 


## How to Win

The aim of the game is to beat the dealer! You can do this by:
    
    - Scoring 21 without the dealer scoring 21
    - Getting a higher score than the dealer (without going bust!)
    - Or the dealer going bust

## The Rules

- Ace is 1 or eleven (automatically selected to ensure you get the highest possible score without going bust)
- A score over 21 is bust!
- 'Hit' deals another card
- 'Stand' moves play onto the dealer
- A score of 21 or over automatically moves play on to the dealer
- The dealer hits until they have a score of 17 or more
- If the dealer and player have an equal score, its a draw
- If the player is bust, the dealer always wins

How to bet: 
- Your bet is placed before the initial deal at the start of each round
- If you win, your bet is doubled and added to your pot
- If you lose, your bet is removed from your pot
- If it's a draw, your bet is returned to your pot
- Your pot starts at £100 and bets can be any whole value up to the current value of your pot
- If you run out of cash the game ends!


## Running the Game

Download the folder and run the index.py file in the root directory (example below).
This game was built using Python 3

```
git clone https://github.com/jemonaghan/blackjack.git
cd blackjack
python3 index.py
```

## Running the Tests

Ensure the project is cloned (see above), then run the following command from the project root directory.

```
python3 -m unittest discover test
```


## Sample Output

```    
.------..------..------..------..------..------..------..------..------.
|B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'

Welcome to Blackjack! Can you beat the dealer and get to 21 without going bust?
    
How much would you like to bet? You have £100
£10
    
Starting hand:

6   Hearts
9   Diamonds
    
Would you like to hit or stand? Enter 'h' or 's'
h

New hand is: 

10  Hearts
6   Hearts
9   Diamonds

Starting hand:

4   Hearts
King    Diamonds


New hand is: 
10  Clubs
4   Hearts
King    Diamonds

The player total is 25
The dealer total is 24

The player is bust! Dealer wins

You have £90 in your pot

Would you like to play another hand of Blackjack? Enter 'y' or 'n'
```

