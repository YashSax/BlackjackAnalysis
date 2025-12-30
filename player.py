from utils import *
from typing import List
import json

def dealer_strategy(dealer_cards: List[Card]):
    hand_value = calculate_hand_value(dealer_cards)
    if hand_value < 17:
        return Decision.HIT
    return Decision.STAND

def player_copy_dealer(player_cards: List[Card], dealer_showing: Card):
    return dealer_strategy(player_cards)    

def player_strategy(player_cards: List[Card], dealer_showing: Card):
    if len(player_cards) == 2:
        if player_cards[0].value == player_cards[1].value:
            if (
                player_cards[0].value in pair_splitting
                and pair_splitting[player_cards[0].value][dealer_showing.value] == "Y"
            ):
                return Decision.SPLIT

    hand_value = calculate_hand_value(player_cards)
    lowest_hand_value = calculate_lowest_hand_value(player_cards)

    # If you've already overshot 21 with aces as 11, then you should use the hard total table
    # even though you have aces.
    if any(card.value == Value.ACE for card in player_cards) and hand_value != lowest_hand_value:
        if hand_value not in soft_totals:
            return Decision.STAND 
        return soft_totals[hand_value][dealer_showing.value]
    else:
        if hand_value not in hard_totals:
            return Decision.STAND
        return hard_totals[hand_value][dealer_showing.value]


if __name__ == "__main__":
    # Test 1: Pair splitting (8,8) vs dealer 6 -> should split
    player_hand = [Card(Suite.HEARTS, Value.EIGHT), Card(Suite.SPADES, Value.EIGHT)]
    dealer_card = Card(Suite.CLUBS, Value.SIX)
    decision = player_strategy(player_hand, dealer_card)
    print(f"Test 1 (8,8 vs 6): {decision} (expected SPLIT)")

    # Test 2: Hard total 16 vs dealer 10 -> should hit
    player_hand = [Card(Suite.HEARTS, Value.TEN), Card(Suite.SPADES, Value.SIX)]
    dealer_card = Card(Suite.CLUBS, Value.TEN)
    decision = player_strategy(player_hand, dealer_card)
    print(f"Test 2 (16 vs 10): {decision} (expected HIT)")

    # Test 3: Soft total A+7 vs dealer 2 -> double down
    player_hand = [Card(Suite.HEARTS, Value.ACE), Card(Suite.DIAMONDS, Value.SEVEN)]
    dealer_card = Card(Suite.CLUBS, Value.TWO)
    decision = player_strategy(player_hand, dealer_card)
    print(f"Test 3 (A+7 vs 2): {decision} (expected DOUBLE_DOWN)")

    # Test 4: Soft total A+9 vs dealer 10 -> stand
    player_hand = [Card(Suite.CLUBS, Value.ACE), Card(Suite.HEARTS, Value.NINE)]
    dealer_card = Card(Suite.SPADES, Value.TEN)
    decision = player_strategy(player_hand, dealer_card)
    print(f"Test 4 (A+9 vs 10): {decision} (expected STAND)")

    # Test 5: Hard total 12 vs dealer 4 -> stand
    player_hand = [Card(Suite.HEARTS, Value.EIGHT), Card(Suite.CLUBS, Value.FOUR)]
    dealer_card = Card(Suite.DIAMONDS, Value.FOUR)
    decision = player_strategy(player_hand, dealer_card)
    print(f"Test 5 (12 vs 4): {decision} (expected STAND)")

    # Test 6: Multiple aces -> stand
    player_hand = [
        Card(Suite.HEARTS, Value.ACE),
        Card(Suite.HEARTS, Value.FIVE),
        Card(Suite.CLUBS, Value.ACE),
        Card(Suite.HEARTS, Value.TEN),
    ]
    dealer_card = Card(Suite.DIAMONDS, Value.SEVEN)
    decision = player_strategy(player_hand, dealer_card)
    print(f"Test 6 (Soft -> Hard 17 vs 7): {decision} (expected STAND)")

    # Test 7: Mine
    player_hand = [Card(Suite.HEARTS, Value.KING), Card(Suite.DIAMONDS, Value.FIVE)]
    dealer_card = Card(Suite.HEARTS, Value.FIVE)
    decision = player_strategy(player_hand, dealer_card)
    print(f"Test 7: {decision}")
