from enum import Enum

class Suit(Enum):
    """
    A suit can have 4 discrete values so it makes sense to use an Enum for it.
    """

    CLUBS = "clubs"
    DIAMONDS = "diamonds"
    HEARTS = "hearts"
    SPADES = "spades"

class Card:
    """
    Card has a suit and a value. Value is a number between 1 and 10.

    TODO: Add logic that enforces the value is valid and throws an exception if it's not.
    """

    def __init__(self, suit: str, value: int):
        self._suit = suit
        self._value = value

    def get_suit(self) -> str:
        return self._suit

    def get_value(self) -> int:
        return self._value

    def print_card(self) -> None:
        print(self.get_suit(), self.get_value())