from classes import *


count_of_players = input_int_count()


players = create_players(count_of_players)

print("List of players:\n")
for i in range(0, count_of_players):
    print(f"{players[i]}\n")

dealer = Player("Dealer")
deck = Deck()
deck.shuffle()

for i in range(0, count_of_players):
    players[i].bet_input()

dealer.hit(deck)
dealer.hit(deck)
print(f"{dealer.owner} take two cards")

for i in range(0, count_of_players):
    players[i].hit(deck)
    players[i].hit(deck)
    print(f"{players[i].owner} take two cards")

print(f"{dealer.owner} has a '{dealer.hand[0]}'\n")

for i in range(0, 100):
    print("\n")

for i in range(0, count_of_players):
    print(f"{players[i].owner}'s cards are '{players[i].hand}'\n")
    while True:
        print("Do you want take a card?")
        if input_yes():
            players[i].hit(deck)
            print(f"{players[i].owner} has a  '{players[i].hand}'")
            print(f"{players[i].owner}'s weight is {players[i].weight_hand()}")
            #     add check losing
            if players[i].weight_hand() > 21:
                print(f"{players[i].owner}'s losing")
                # add something after checking
                break
        else:
            for i in range(0, 20):
                print("\n")
            break

while dealer.weight_hand() < 17:
    dealer.hit(deck)
    print(f"{dealer.owner} has a '{dealer.hand[0]}'")
    print(f"{dealer.owner}'s weight is {dealer.weight_hand()}")
    if dealer.weight_hand() > 21:
        print(f"{dealer.owner}'s losing")
        # add something after checking
        break

print(f"{dealer.owner} has a '{dealer.hand}'")
print(f"{dealer.owner}'s weight is {dealer.weight_hand()}")
print("\n")

for i in range(0, count_of_players):
    print(f"{players[i].owner} has a '{players[i].hand}'")
    print(f"{players[i].owner}'s weight is {players[i].weight_hand()}")
    print("\n")

print("Do you want to play again? 'Yes' or 'No'")
if input_yes():
    pass
else:
    pass

players.append(dealer)
# players = sorted(players, key=lambda player: player.weight_hand(), reverse=True)


winners = get_winners(players)


for i in range(0, 20):
    print("\n")

print("Winners\n")
for i in range(0, len(winners)):
    print(f"{winners[i]}")

change_money(_players=players, _winners=winners)
