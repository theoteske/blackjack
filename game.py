from player import UserPlayer, Dealer
from deck import Deck

class GameRound:
    """
    GameRound is responsible for controlling the flow of the game. It is provided a
    UserPlayer, a Dealer, and a Deck. It prompts the user to input a bet amount, deals
    the initial cards, and cleans up at the end of a round.
    """

    def __init__(self, user: UserPlayer, dealer: Dealer, deck: Deck):
        self._user = user
        self._dealer = dealer
        self._deck = deck

    def get_user_bet(self) -> int:
        amount = int(input("Enter a wager: "))
        return amount

    def deal_initial_cards(self) -> None:
        for _ in range(2):
            self._user.add_card(self._deck.draw())
            self._dealer.add_card(self._deck.draw())

        print("Player hand: ")
        self._user.get_hand().print_hand()
        print("Dealer's face-up card: ")
        self._dealer.get_hand().get_cards()[0].print_card()

    def cleanup_round(self) -> None:
        self._user.clear_hand()
        self._dealer.clear_hand()
        print("Your balance: ", self._user.get_balance())

    def play(self) -> None:
        # shuffle deck
        self._deck.shuffle()

        # if user has run out of money, the game ends
        if self._user.get_balance() <= 0:
            print("You have insufficient funds to continue playing.")
            return

        # otherwise, determine wager
        user_bet = self.get_user_bet()
        self._user.place_bet(user_bet)

        # deal the first two cards to user and dealer
        self.deal_initial_cards()

        # user makes moves
        while self._user.make_move():
            card_drawn = self._deck.draw()
            print("You drew a ", card_drawn.get_value(), " of ", card_drawn.get_suit())
            self._user.add_card(card_drawn)
            print("Your score is now: ", self._user.get_hand().get_score())

        if self._user.get_hand().get_score() > 21:
            print("You busted!")
            self.cleanup_round()
            return

        # dealer makes moves
        while self._dealer.make_move():
            card_drawn = self._deck.draw()
            print("Dealer drew a ", card_drawn.get_value(), " of ", card_drawn.get_suit())
            self._dealer.add_card(card_drawn)
            print("Dealer's score is now: ", self._dealer.get_hand().get_score())

        # determine winner
        user_score = self._user.get_hand().get_score()
        dealer_score = self._dealer.get_hand().get_score()
        if dealer_score > 21 or user_score > dealer_score:
            print("You win!")
            self._user.receive_winnings(user_bet * 2)
        elif dealer_score > user_score:
            print("You lost!")
        else:
            print("It's a tie!")
            self._user.receive_winnings(user_bet)
        self.cleanup_round()