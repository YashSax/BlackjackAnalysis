import random
from utils import *
from player import *
from typing import Callable, List
from tqdm import tqdm

CARDS_PER_DECK = 52

class BlackjackGame:
    def __init__(
        self, num_decks: int, dealer_strategy: Callable, player_strategy: Callable
    ):
        self.num_decks = num_decks
        self.RESET_CUTOFF = int(CARDS_PER_DECK * num_decks * 0.2)
        self.reset()

        player_first = self.draw_card()
        self.dealer_showing = self.draw_card()
        player_second = self.draw_card()
        dealer_hidden = self.draw_card()

        # print("Dealer showing:", self.dealer_showing)

        self.player_cards = [player_first, player_second]
        self.dealer_cards = [self.dealer_showing, dealer_hidden]

        self.dealer_strategy = dealer_strategy
        self.player_strategy = player_strategy

    def reset(self):
        self.deck = [
            Card(suite=suite, value=value)
            for suite in Suite
            for value in Value
            for _ in range(self.num_decks)
        ]

        random.shuffle(self.deck)

    def draw_card(self):
        assert len(self.deck) > 0, "There must be cards in a deck to draw from it!"
        return self.deck.pop()

    def play(self, bet_amount: int) -> int:
        player_hand_outcomes = self.play_player_hand(self.player_cards.copy(), self.dealer_showing, bet_amount)
        # print("Player hand outcomes:", player_hand_outcomes)

        money_won = -1 * sum(outcome.money_bet for outcome in player_hand_outcomes)

        # If the player busts on every hand, then there's no need to run the dealer's hand.
        if all(outcome.value > 21 for outcome in player_hand_outcomes):
            # print("Player busts! Wins", money_won)
            return money_won

        dealer_value = self.play_dealer_hand(self.dealer_cards.copy())
        # print("Dealer value:", dealer_value)
        for outcome in player_hand_outcomes:
            if outcome.value > 21:
                continue

            if dealer_value > 21:
                money_won += outcome.money_bet * 2
            elif outcome.value > dealer_value:
                money_won += outcome.money_bet * 2
            elif outcome.value == dealer_value:
                money_won += outcome.money_bet

        # print("Player wins:", money_won)
        return money_won

    def play_player_hand(self, player_cards: List[Card], dealer_showing: Card, bet_amount: int) -> List[HandOutcome]:
        decision = self.player_strategy(player_cards, dealer_showing)
        # print("Decision =", decision)
        while decision == Decision.HIT:
            player_cards.append(self.draw_card())
            hand_value = calculate_hand_value(player_cards)
            if hand_value > 21:
                return [HandOutcome(
                    cards=player_cards,
                    value=hand_value,
                    money_bet=bet_amount
                )]
            decision = self.player_strategy(player_cards, dealer_showing)
            # print("Decision =", decision)

        if decision == Decision.STAND:
            hand_value = calculate_hand_value(player_cards)
            return [HandOutcome(
                cards=player_cards,
                value=hand_value,
                money_bet=bet_amount
            )]
        elif decision == Decision.DOUBLE_DOWN:
            new_card = self.draw_card()
            player_cards.append(new_card)
            return [HandOutcome(
                cards=player_cards,
                value = calculate_hand_value(player_cards),
                money_bet=bet_amount * 2
            )]
        else:
            assert decision == Decision.SPLIT
            assert len(player_cards) == 2 and player_cards[0].value == player_cards[1].value, "Hand must contain only two cards of the same value!"

            first_half = self.play_player_hand([player_cards[0], self.draw_card()], self.dealer_showing, bet_amount)
            second_half = self.play_player_hand([player_cards[1], self.draw_card()], self.dealer_showing, bet_amount)

            return first_half + second_half

    def play_dealer_hand(self, dealer_cards: List[Card]) -> int:
        decision = self.dealer_strategy(dealer_cards)
        while decision == Decision.HIT:
            dealer_cards.append(self.draw_card())
            decision = self.dealer_strategy(dealer_cards)

        # print("Dealer cards:", dealer_cards)
        return calculate_hand_value(dealer_cards)

if __name__ == "__main__":
    BUY_IN = 10
    NUM_RUNS = 100_000

    money_won = 0
    for _ in tqdm(range(NUM_RUNS)):
        game = BlackjackGame(
            num_decks=6,
            dealer_strategy=dealer_strategy,
            player_strategy=player_strategy # swap this to change the player strategy
        )

        money_won += game.play(BUY_IN)

    winnings_per_round = money_won / NUM_RUNS

    print("Results for using the fancy table:")
    print(f"Running for {NUM_RUNS} runs, strategy wins ${money_won}")
    print(f"Money put in: {NUM_RUNS * BUY_IN}")
    print(f"On average, this strategy gains {winnings_per_round} per round")

    if winnings_per_round > 0:
        edge = winnings_per_round / BUY_IN * 100
        print(f"This is a +{edge:.2f}% edge")
    elif winnings_per_round == 0:
        print("This is a net neutral strategy")
    else:
        edge = -1 * winnings_per_round / BUY_IN * 100
        print(f"This is a -{edge:.2f}% edge")
