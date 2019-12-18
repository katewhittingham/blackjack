
import random
from itertools import product



class Deck(object):
 def __init__(self, ranks=None, suits=None):
        if ranks is None:
            ranks = range(2, 15)
        if suits is None:
            suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.deck = []
        for r in ranks:
            for s in suits:
                self.deck.append(r, s)

def deal(self, n):
        return random.sample(self.deck, n)


hand = []
comphand = []

hand.append(deck.deal(2))
comphand.append(deck.deal(2))

while sum(comphand) < 16:
 comphand.append(deck.deal(1))



print("Your cards are " *hand)

while sum(hand) < 22:
 if input("Would you like to draw a card?") == "yes":
  hand.append(deck.deal(1))
  print("Your cards are", *hand)


 else:
    if sum(hand) > sum(comphand):
     print("You win!")

    elif sum(hand) > 21:
     print("You went bust!")

    elif sum(hand) == sum(comphand):
     print("A draw.")

    else:
     print("You lose!")
