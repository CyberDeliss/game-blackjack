from classes import *
# from logic import *


player1 = Player()
dealer = Player("Dealer")
deck = Deck()
deck.shuffle()

# bet = player1.bet_input()

take_a_card(dealer, deck)
take_a_card(dealer, deck)
print(f"{dealer.owner} take two cards")

take_a_card(player1, deck)
take_a_card(player1, deck)
print(f"{player1.owner} take two cards")

print(f"{dealer.owner} has a '{dealer.hand[0]}'\n"
      f"Your cards is '{player1.hand}'\n"
      f" What will you do?\n\n"
      f"")
      # f"Will you take a card? ('yes/y' or 'no/n')")


print(f"{player1.hand[0].get_weight()}")
print(f"{player1.weight_hand()}")
