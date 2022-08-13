import random


# diamonds # бубны (♦)
# spades # пики (♠)
# hearts # червы (♥)
# clubs # трефы (♣)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.weight = 0

    def __repr__(self):
        return f"{self.suit}, {self.value}"

    def get_weight(self):
        # self.weight
        try:
            if int(self.value) in range(2, 11):
                self.weight = self.value
        except ValueError:
            if self.value in ("J", "Q", "K"):
                self.weight = 10
            else:
                self.weight = 11
        return self.weight


class Deck:
    suits = ["hearts", "diamonds", "clubs", "spades"]
    num_of_cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    def __init__(self):
        self.deck = [Card(suit, value) for suit in self.suits for value in self.num_of_cards]
        print(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
        print(self.deck)

    def __len__(self):
        return len(self.deck)


class Player:
    def __init__(self, _owner="Ganya", _balance=100):
        self.owner = _owner
        if self.owner == "Dealer":
            self.balance = 100000000000
        else:
            self.balance = _balance
        self.hand = []
        self.bet = 0

    def __str__(self):
        return f'Owner: {self.owner}\nBalance: {self.balance}'

    def deposit(self, _num):
        """
        Player's balance grow up on _num
        :param _num:
        :return: none.
        """
        self.balance += _num

    def make_a_bet(self):
        if self.balance >= self.bet:
            self.balance -= self.bet
        else:
            print(f"Your balance is low than {self.bet}")

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
            total += self.hand[i].get_weight()
        return total

    def hit(self, _deck):
        """
        append element Card (suit, value) for example "diamonds, K" to player's hand
        and delete it from _deck
        :return: none.
        """
        i = random.randint(0, len(_deck) - 1)
        card = _deck.deck.pop(i)
        self.hand.append(card)

    def stay(self):
        pass




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


def create_players(_count):
    """
    function creates array of players
    :return: array of players
    """
    players = []
    for i in range(0, _count):
        # Add input Name and balance for players
        player_name = input_name()
        player_balance = 10
        player = Player(player_name, player_balance)
        players.append(player)
    return players


def get_winners(_players):
    winners = list(filter(lambda player: player.weight_hand() < 22, _players))
    winners = list(filter(lambda player: player.weight_hand() ==
                                         max(winners, key=lambda win_player: win_player.weight_hand()).weight_hand(),
                          winners))
    return winners


def change_money(_players, _winners):
    for player in _players:
        if player in _winners:
            player.balance += player.bet
        else:
            player.balance -= player.bet
        print(f"{player.owner}'s balance is {player.balance}\n")


class Game:

    def __init__(self):
        self.dealer = Player("Dealer")

        self.deck = Deck()

    def start_game(self):
        self.deck.shuffle()

    def circle(self):
        pass

    def __str__(self):
        # print info about all players
        pass

    def end_circle(self):
        pass

