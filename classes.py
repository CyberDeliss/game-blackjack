import random
from copy import copy


# diamonds # бубны (♦)
# spades # пики (♠)
# hearts # червы (♥)
# clubs # трефы (♣)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        try:
            if int(self.value) in range(2, 11):
                self.weight = self.value
        except ValueError:
            if self.value in ("J", "Q", "K"):
                self.weight = 10
            else:
                self.weight = 11

    def __repr__(self):
        return f"{self.suit}, {self.value}"

    def change_weight(self):
        if self.weight == 11:
            self.weight = 1
        elif self.weight == 1:
            self.weight = 11


class Deck:
    suits = ["hearts", "diamonds", "clubs", "spades"]
    num_of_cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    def __init__(self):
        self.deck = [Card(suit, value) for suit in self.suits for value in self.num_of_cards]

    def shuffle(self):
        random.shuffle(self.deck)

    def __len__(self):
        return len(self.deck)

    def deal(self):
        """
        return last Card from self and delete Card
        :return: card Card.
        """
        card = self.deck.pop()
        return card


class Player:
    def __init__(self, _owner="Name", _balance=100):
        self.owner = _owner
        self.dealer = False
        self.balance = _balance
        self.hand = []
        self.bet = 0

    def __str__(self):
        return f"Owner: {self.owner}\nBalance: {self.balance}"

    def deposit(self, _num):
        """
        Player's balance grow up on _num
        :param _num:
        :return: none.
        """
        self.balance += _num

    def print_balance(self):
        print(f"Your balance is {self.balance}")

    def bet_input(self):
        """
        Player input a bet
        self.bet = input <= self.balance
        :return: none.
        """
        while True:
            bet = input(f"Please, make a bet from 1 to {self.balance}\n")
            try:
                bet = int(bet)
                if bet <= 0:
                    print("Bet has to be higher than 0")
                    continue

                if 1 <= bet <= self.balance:
                    self.bet = bet
                    break
                else:
                    print(f"Your balance is lower than {bet}")
            except ValueError:
                print("Value Error")
                continue
            except TypeError:
                print("Type Error")
                continue

    def weight_hand(self):
        total = 0
        for i in range(0, len(self.hand)):
            total += self.hand[i].weight
        return total

    def hit(self, _deck):
        """
        append element Card (suit, value) for example "diamonds, K" to player's hand
        and delete it from _deck
        :return: none.
        """
        self.hand.append(_deck.deal())

    def stay(self):
        pass

    def change_the_weight(self):
        changes = False
        for card in self.hand:
            try:
                if card.value == "A":
                    print(f"Do you want to change the weight of the card {card}?")
                    if input_yes():
                        card.change_weight()
                        changes = True
            except ValueError:
                continue
            except:
                continue
        return changes


def input_yes():
    """
    True if player input in ("yes", "y", "+")
    False if player input in ("no", "n", "-")
    :return: True or False
    """
    while True:
        try:
            answer = input("('yes/y' or 'no/n')\n").lower()
            if answer.lower() in ("yes", "y", "+"):
                return True
            if answer.lower() in ("no", "n", "-"):
                return False
        except:
            continue


def input_int_count():
    """
    input from player
    :return: integer number
    """
    while True:
        count = input("Please, input integer number\n")
        try:
            count = int(count)
            return count
        except ValueError:
            print("Value Error")
            continue
        except TypeError:
            print("Type Error")
            continue


def input_name():
    while True:
        name = input("Please, input name\n")
        try:
            name = name.lower()
            name = name.capitalize()
            print(f"Your name is {name}?\n")
            if input_yes():
                return name
            else:
                continue
        except ValueError:
            print("Value Error")
            continue
        except TypeError:
            print("Type Error")
            continue


class Game:
    def __init__(self):
        self.players = []
        self.dealer = Player("Dealer")
        self.dealer.dealer = True
        self.deck = Deck()
        self.winners = []
        self.losers = []

    def start_game(self, _count_players):
        self.create_players(_count_players)

    def loop(self):
        self.deck.shuffle()
        self.players_bet()

        self.dealer.hit(self.deck)
        self.dealer.hit(self.deck)

        print(f"{self.dealer.owner} has a '{self.dealer.hand[0]}'\n")

        for player in self.players:
            player.hit(self.deck)
            player.hit(self.deck)

        for player in self.players:
            self.player_turn(player)

        self.dealer_turn()

    def end_loop(self):
        self.get_winners()
        self.get_losers()
        self.change_money()
        self.print_info()

    def create_players(self, _count):
        """
        function creates array of players in Game (self.players)
        :return: None
        """
        for i in range(0, _count):
            player_name = input_name()          # input Name for player
            player_balance = 10                 # start balance

            player = Player(player_name, player_balance)
            self.players.append(player)

    def players_bet(self):
        for i in range(0, len(self.players)):
            self.players[i].bet_input()

    def player_turn(self, _player):
        print(f"{_player.owner}'s cards are '{_player.hand}'\n")
        print(f"{_player.owner}'s weight is {_player.weight_hand()}")

        while True:
            print("Do you want take a card?")
            if input_yes():
                _player.hit(self.deck)
                print(f"{_player.owner} has a  '{_player.hand}'")
                print(f"{_player.owner}'s weight is {_player.weight_hand()}")

                #     add check losing
                if _player.weight_hand() > 21:
                    if _player.change_the_weight():
                        if _player.weight_hand() <= 21:
                            print(f"{_player.owner}'s cards are '{_player.hand}'\n")
                            print(f"{_player.owner}'s weight is {_player.weight_hand()}")
                            continue
                        else:
                            break
                    else:
                        print(f"{_player.owner}'s losing")
                        # add something after checking
                        break
            else:
                for i in range(0, 20):
                    print("\n")
                break

    def dealer_turn(self):
        while self.dealer.weight_hand() < 17:
            self.dealer.hit(self.deck)

            print(f"{self.dealer.owner} has a '{self.dealer.hand[0]}'")
            print(f"{self.dealer.owner}'s weight is {self.dealer.weight_hand()}")

            if self.dealer.weight_hand() > 21:
                print(f"{self.dealer.owner}'s losing")
                # add something after checking
                break

    def get_winners(self):
        temp_players = copy(self.players)
        temp_players.append(self.dealer)
        self.winners = list(filter(lambda player: player.weight_hand() < 22, temp_players))
        self.winners = list(filter(lambda player: player.weight_hand() ==
                                   max(self.winners, key=lambda win_player: win_player.weight_hand()).weight_hand(),
                            self.winners))

    def get_losers(self):
        for player in self.players:
            if not (player in self.winners):
                self.losers.append(player)

    def change_money(self):
        for player in self.players:
            if player in self.winners:
                player.balance += player.bet
            else:
                player.balance -= player.bet
                if player.balance <= 0:
                    print(f"It is game over for {player.owner}. You spent all your money\n")
                    self.players.remove(player)

    def print_info(self):
        print("Winners:\n")
        for player in self.winners:
            print(f"{player.owner} has a '{player.hand}'")
            print(f"{player.owner}'s weight is {player.weight_hand()}")
            print(f"{player.owner}'s balance is {player.balance}")
            print("\n")

        print("Who loosed but can continue playing:\n")

        for player in self.losers:
            if player.balance > 0:
                print(f"{player.owner} has a '{player.hand}'")
                print(f"{player.owner}'s weight is {player.weight_hand()}")
                print(f"{player.owner}'s balance is {player.balance}")
                print("\n")

    def restart_game(self):
        self.winners = []
        self.losers = []
        self.deck = Deck()

        for player in self.players:
            player.hand = []
            player.bet = 0

        self.dealer.hand = []


