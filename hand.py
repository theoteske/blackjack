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
        self._has_ace = False

    def add_card(self, new_card: Card) -> None:
        self._cards.append(new_card)

        # consider case where new_card is an ace
        if new_card.get_value() == 1:
            self._has_ace = True
            self._score += 11 if self._score < 11 else 1
        else:
            self._score += new_card.get_value()

        # if there is an ace in the hand, we have to recount our score if we go over 21
        if self._has_ace and self._score > 21:
            self._score = 0
            for card in self._cards:
                self._score += card.get_value()

    def get_score(self) -> int:
        return self._score

    def get_cards(self) -> List[Card]:
        return self._cards

    def print_hand(self) -> None:
        for card in self.get_cards():
            print(card.get_suit(), card.get_value())