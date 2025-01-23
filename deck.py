from random import randint
from card import Suit, Card

class Deck:
    """
    Deck has an array of cards and is responsible for shuffling and drawing cards. We
    build the deck by iterating 13 times for each suit. This means that we cannot currently
    distinguish between a 10, Jack, Queen, and King.

    TODO: Add a name field to the Card class to distinguish between 10s and face cards.
    """

    def __init__(self):
        self._cards = []

        # fill the deck with cards
        for suit in Suit:
            for value in range(1, 14):
                self._cards.append(Card(suit, min(value, 10)))

    def draw(self):
        return self._cards.pop()

    def shuffle(self):
        for i in range(len(self._cards)):
            j = randint(0, 51)
            self._cards[i], self._cards[j] = self._cards[j], self._cards[i]