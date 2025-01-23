from player import UserPlayer, Dealer
from hand import Hand
from deck import Deck
from game import GameRound

"""
Run the game until the user runs out of money.
"""

user = UserPlayer(Hand())
dealer = Dealer(Hand())

while user.get_balance() > 0:
    GameRound(user, dealer, Deck()).play()