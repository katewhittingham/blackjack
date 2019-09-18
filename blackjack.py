import random

deck = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]

for card in deck:
    if card == "ace": card == 1
    if card == "jack": card == 10
    if card == "queen": card == 10
    if card == "king": card == 10

c1 = random.choice(deck)
c2 = random.choice(deck)


comp1 = random.choice(deck)
comp2 = random.choice(deck)

comphand = [comp1, comp2]

while sum(comphand) < 16:
 comphand.append(random.choice(deck))

hand = [c1, c2]

count = 2


print("Your cards are ", c1, " and ", c2)

while sum(hand) < 22:
 if input("Would you like to draw a card?") == "yes":
  hand.append(random.choice(deck))
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
