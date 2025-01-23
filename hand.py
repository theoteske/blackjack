from card import Card
from typing import List

class Hand:
    """
    A Hand contains an array of Card objects, and a total score, which is the sum of the
    values of all the Card objects. Every time we add a card, we recalculate the total
    score. We also specially handle the case when the card being added is an ace.

    TODO: Consider making a separate class to handle printing the cards (Single Responsibility Principle).
    """

    def __init__(self):
        self._score = 0
        self._cards = []

    def add_card(self, new_card: Card) -> None:
        self._cards.append(new_card)

        # consider case where new_card is an ace
        # TODO: fix bug, 2 and Ace initial hand then 10 results in bust currently
        if new_card.get_value() == 1:
            self._score += 1 if self._score >= 11 else 11
        else:
            self._score += new_card.get_value()

        # TODO: do we need to print, now it's only here for convenience
        print("Score: ", self._score)

    def get_score(self) -> int:
        return self._score

    def get_cards(self) -> List[Card]:
        return self._cards

    def print_hand(self) -> None:
        for card in self.get_cards():
            print(card.get_suit(), card.get_value())