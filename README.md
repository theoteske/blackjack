# Blackjack

A game of blackjack that you can play in the command line.

How many cards (how many decks)?

What happens when we run out of cards in the deck?
Shuffle deck every time we run out. At the end of a round, we pass a new deck into the GameRound class.

How many players?
Two, user and dealer.

How are we implementing gambling/score keeping?
Player can wager however much they want, if they win they get the amount they wagered.

Consider making another enum for type of card (i.e. if we had a name attribute for the card class) to distinguish between 10, Jack, Queen, King, Ace, etc.

In this same vein, consider making some kind of graphical display of the cards to the user.
