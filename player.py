from abc import ABC, abstractmethod
from card import Card
from hand import Hand

class Player(ABC):
    """
    Abstract class which has a Hand and can make a move. Dealer and UserPlayer classes
    extend this class and override the abstract make_move() method.
    """

    def __init__(self, hand: Hand):
        self._hand = hand

    def get_hand(self) -> Hand:
        return self._hand

    def clear_hand(self) -> None:
        self._hand = Hand()

    def add_card(self, new_card: Card) -> None:
        self._hand.add_card(new_card)

    @abstractmethod
    def make_move(self) -> bool:
        pass

class UserPlayer(Player):
    """
    The UserPlayer has a balance and can place a bet. It overrides make_move() by prompting
    the user for input and returns True to hit (draw another card), or False to stand.
    """

    def __init__(self, hand: Hand, balance: int = 1000):
        super().__init__(hand)
        self._balance = balance

    def get_balance(self) -> int:
        return self._balance

    def place_bet(self, amount: int) -> int:
        # verify that user has sufficient funds
        if amount > self._balance:
            raise ValueError("Insufficient funds. Please wager a smaller amount.")

        self._balance -= amount
        return amount

    def receive_winnings(self, amount: int) -> None:
        self._balance += amount

    def make_move(self):
        if self.get_hand().get_score() >= 21:
            return False

        move = input("Draw another card? [y/n]")
        return move == 'y'

class Dealer(Player):
    """
    The Dealer doesn't place bets or receive winnings. They will only draw cards until their
    hand value is greater than or equal to a target score, which is the value of the user
    player's hand or 17, whichever is greater.

    We can't pass target_score in the constructor because the Dealer will have to update it
    after the user draws.

    TODO: Consider making Dealer's play automatic, so they stand at 17 or more and hit at 16 or below.
    """

    def __init__(self, hand: Hand):
        super().__init__(hand)
        self._target_score = 17

    def update_target_score(self, new_target_score: int) -> None:
        self._target_score = max(self._target_score, new_target_score)

    def make_move(self):
        return self.get_hand().get_score() < self._target_score
