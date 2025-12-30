from enum import Enum
from dataclasses import dataclass
from typing import List

class Suite(Enum):
    HEARTS = "hearts"
    SPADES = "spades"
    DIAMONDS = "diamonds"
    CLUBS = "clubs"


class Value(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class Decision(Enum):
    HIT = 0
    STAND = 1
    SPLIT = 2
    DOUBLE_DOWN = 3

value_map = {
    Value.TWO: 2,
    Value.THREE: 3,
    Value.FOUR: 4,
    Value.FIVE: 5,
    Value.SIX: 6,
    Value.SEVEN: 7,
    Value.EIGHT: 8,
    Value.NINE: 9,
    Value.TEN: 10,
    Value.JACK: 10,
    Value.QUEEN: 10,
    Value.KING: 10,
    Value.ACE: 11,
}


@dataclass
class Card:
    suite: Suite
    value: Value

    def __repr__(self):
        return f"{self.value} of {self.suite}"

@dataclass
class HandOutcome:
    cards: List[Card]
    value: int
    money_bet: int

def calculate_hand_value(cards: List[Card]) -> int:
    total = 0
    num_aces = 0
    for card in cards:
        total += value_map[card.value]
        num_aces += card.value == Value.ACE

    while num_aces and total > 21:
        num_aces -= 1
        total -= 10

    return total    

def calculate_lowest_hand_value(cards: List[Card]) -> int:
    total = 0
    for card in cards:
        total += 1 if card.value == Value.ACE else value_map[card.value]
    return total

hard_totals = {
    17: {
        Value.TWO: Decision.STAND,
        Value.THREE: Decision.STAND,
        Value.FOUR: Decision.STAND,
        Value.FIVE: Decision.STAND,
        Value.SIX: Decision.STAND,
        Value.SEVEN: Decision.STAND,
        Value.EIGHT: Decision.STAND,
        Value.NINE: Decision.STAND,
        Value.TEN: Decision.STAND,
        Value.JACK: Decision.STAND,
        Value.QUEEN: Decision.STAND,
        Value.KING: Decision.STAND,
        Value.ACE: Decision.STAND,
    },
    16: {
        Value.TWO: Decision.STAND,
        Value.THREE: Decision.STAND,
        Value.FOUR: Decision.STAND,
        Value.FIVE: Decision.STAND,
        Value.SIX: Decision.STAND,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    15: {
        Value.TWO: Decision.STAND,
        Value.THREE: Decision.STAND,
        Value.FOUR: Decision.STAND,
        Value.FIVE: Decision.STAND,
        Value.SIX: Decision.STAND,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    14: {
        Value.TWO: Decision.STAND,
        Value.THREE: Decision.STAND,
        Value.FOUR: Decision.STAND,
        Value.FIVE: Decision.STAND,
        Value.SIX: Decision.STAND,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    13: {
        Value.TWO: Decision.STAND,
        Value.THREE: Decision.STAND,
        Value.FOUR: Decision.STAND,
        Value.FIVE: Decision.STAND,
        Value.SIX: Decision.STAND,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    12: {
        Value.TWO: Decision.HIT,
        Value.THREE: Decision.HIT,
        Value.FOUR: Decision.STAND,
        Value.FIVE: Decision.STAND,
        Value.SIX: Decision.STAND,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    11: {
        Value.TWO: Decision.DOUBLE_DOWN,
        Value.THREE: Decision.DOUBLE_DOWN,
        Value.FOUR: Decision.DOUBLE_DOWN,
        Value.FIVE: Decision.DOUBLE_DOWN,
        Value.SIX: Decision.DOUBLE_DOWN,
        Value.SEVEN: Decision.DOUBLE_DOWN,
        Value.EIGHT: Decision.DOUBLE_DOWN,
        Value.NINE: Decision.DOUBLE_DOWN,
        Value.TEN: Decision.DOUBLE_DOWN,
        Value.JACK: Decision.DOUBLE_DOWN,
        Value.QUEEN: Decision.DOUBLE_DOWN,
        Value.KING: Decision.DOUBLE_DOWN,
        Value.ACE: Decision.DOUBLE_DOWN,
    },
    10: {
        Value.TWO: Decision.DOUBLE_DOWN,
        Value.THREE: Decision.DOUBLE_DOWN,
        Value.FOUR: Decision.DOUBLE_DOWN,
        Value.FIVE: Decision.DOUBLE_DOWN,
        Value.SIX: Decision.DOUBLE_DOWN,
        Value.SEVEN: Decision.DOUBLE_DOWN,
        Value.EIGHT: Decision.DOUBLE_DOWN,
        Value.NINE: Decision.DOUBLE_DOWN,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    9: {
        Value.TWO: Decision.HIT,
        Value.THREE: Decision.DOUBLE_DOWN,
        Value.FOUR: Decision.DOUBLE_DOWN,
        Value.FIVE: Decision.DOUBLE_DOWN,
        Value.SIX: Decision.DOUBLE_DOWN,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    8: {
        Value.TWO: Decision.HIT,
        Value.THREE: Decision.HIT,
        Value.FOUR: Decision.HIT,
        Value.FIVE: Decision.HIT,
        Value.SIX: Decision.HIT,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
}

soft_totals = {
    20: {  # A+9
        Value.TWO: Decision.STAND,
        Value.THREE: Decision.STAND,
        Value.FOUR: Decision.STAND,
        Value.FIVE: Decision.STAND,
        Value.SIX: Decision.STAND,
        Value.SEVEN: Decision.STAND,
        Value.EIGHT: Decision.STAND,
        Value.NINE: Decision.STAND,
        Value.TEN: Decision.STAND,
        Value.JACK: Decision.STAND,
        Value.QUEEN: Decision.STAND,
        Value.KING: Decision.STAND,
        Value.ACE: Decision.STAND,
    },
    19: {  # A+8
        Value.TWO: Decision.STAND,
        Value.THREE: Decision.DOUBLE_DOWN,
        Value.FOUR: Decision.DOUBLE_DOWN,
        Value.FIVE: Decision.DOUBLE_DOWN,
        Value.SIX: Decision.DOUBLE_DOWN,
        Value.SEVEN: Decision.STAND,
        Value.EIGHT: Decision.STAND,
        Value.NINE: Decision.STAND,
        Value.TEN: Decision.STAND,
        Value.JACK: Decision.STAND,
        Value.QUEEN: Decision.STAND,
        Value.KING: Decision.STAND,
        Value.ACE: Decision.STAND,
    },
    18: {  # A+7
        Value.TWO: Decision.DOUBLE_DOWN,
        Value.THREE: Decision.DOUBLE_DOWN,
        Value.FOUR: Decision.DOUBLE_DOWN,
        Value.FIVE: Decision.DOUBLE_DOWN,
        Value.SIX: Decision.DOUBLE_DOWN,
        Value.SEVEN: Decision.STAND,
        Value.EIGHT: Decision.STAND,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    17: {  # A+6
        Value.TWO: Decision.HIT,
        Value.THREE: Decision.DOUBLE_DOWN,
        Value.FOUR: Decision.DOUBLE_DOWN,
        Value.FIVE: Decision.DOUBLE_DOWN,
        Value.SIX: Decision.DOUBLE_DOWN,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    16: {  # A+5
        Value.TWO: Decision.HIT,
        Value.THREE: Decision.DOUBLE_DOWN,
        Value.FOUR: Decision.DOUBLE_DOWN,
        Value.FIVE: Decision.DOUBLE_DOWN,
        Value.SIX: Decision.DOUBLE_DOWN,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    15: {  # A+4
        Value.TWO: Decision.HIT,
        Value.THREE: Decision.HIT,
        Value.FOUR: Decision.DOUBLE_DOWN,
        Value.FIVE: Decision.DOUBLE_DOWN,
        Value.SIX: Decision.DOUBLE_DOWN,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    14: {  # A+3
        Value.TWO: Decision.HIT,
        Value.THREE: Decision.HIT,
        Value.FOUR: Decision.HIT,
        Value.FIVE: Decision.DOUBLE_DOWN,
        Value.SIX: Decision.DOUBLE_DOWN,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
    13: {  # A+2
        Value.TWO: Decision.HIT,
        Value.THREE: Decision.HIT,
        Value.FOUR: Decision.HIT,
        Value.FIVE: Decision.DOUBLE_DOWN,
        Value.SIX: Decision.DOUBLE_DOWN,
        Value.SEVEN: Decision.HIT,
        Value.EIGHT: Decision.HIT,
        Value.NINE: Decision.HIT,
        Value.TEN: Decision.HIT,
        Value.JACK: Decision.HIT,
        Value.QUEEN: Decision.HIT,
        Value.KING: Decision.HIT,
        Value.ACE: Decision.HIT,
    },
}

pair_splitting = {
    Value.ACE: {
        Value.TWO: "Y",
        Value.THREE: "Y",
        Value.FOUR: "Y",
        Value.FIVE: "Y",
        Value.SIX: "Y",
        Value.SEVEN: "Y",
        Value.EIGHT: "Y",
        Value.NINE: "Y",
        Value.TEN: "Y",
        Value.JACK: "Y",
        Value.QUEEN: "Y",
        Value.KING: "Y",
        Value.ACE: "Y",
    },
    Value.TEN: {
        Value.TWO: "N",
        Value.THREE: "N",
        Value.FOUR: "N",
        Value.FIVE: "N",
        Value.SIX: "N",
        Value.SEVEN: "N",
        Value.EIGHT: "N",
        Value.NINE: "N",
        Value.TEN: "N",
        Value.JACK: "N",
        Value.QUEEN: "N",
        Value.KING: "N",
        Value.ACE: "N",
    },
    Value.NINE: {
        Value.TWO: "Y",
        Value.THREE: "Y",
        Value.FOUR: "Y",
        Value.FIVE: "Y",
        Value.SIX: "Y",
        Value.SEVEN: "N",
        Value.EIGHT: "Y",
        Value.NINE: "Y",
        Value.TEN: "N",
        Value.JACK: "N",
        Value.QUEEN: "N",
        Value.KING: "N",
        Value.ACE: "N",
    },
    Value.EIGHT: {
        Value.TWO: "Y",
        Value.THREE: "Y",
        Value.FOUR: "Y",
        Value.FIVE: "Y",
        Value.SIX: "Y",
        Value.SEVEN: "Y",
        Value.EIGHT: "Y",
        Value.NINE: "Y",
        Value.TEN: "Y",
        Value.JACK: "Y",
        Value.QUEEN: "Y",
        Value.KING: "Y",
        Value.ACE: "Y",
    },
    Value.SEVEN: {
        Value.TWO: "Y",
        Value.THREE: "Y",
        Value.FOUR: "Y",
        Value.FIVE: "Y",
        Value.SIX: "Y",
        Value.SEVEN: "Y",
        Value.EIGHT: "N",
        Value.NINE: "N",
        Value.TEN: "N",
        Value.JACK: "N",
        Value.QUEEN: "N",
        Value.KING: "N",
        Value.ACE: "N",
    },
    Value.SIX: {
        Value.TWO: "Y",
        Value.THREE: "Y",
        Value.FOUR: "Y",
        Value.FIVE: "Y",
        Value.SIX: "Y",
        Value.SEVEN: "N",
        Value.EIGHT: "N",
        Value.NINE: "N",
        Value.TEN: "N",
        Value.JACK: "N",
        Value.QUEEN: "N",
        Value.KING: "N",
        Value.ACE: "N",
    },
    Value.FIVE: {
        Value.TWO: "N",
        Value.THREE: "N",
        Value.FOUR: "N",
        Value.FIVE: "N",
        Value.SIX: "N",
        Value.SEVEN: "N",
        Value.EIGHT: "N",
        Value.NINE: "N",
        Value.TEN: "N",
        Value.JACK: "N",
        Value.QUEEN: "N",
        Value.KING: "N",
        Value.ACE: "N",
    },
    Value.FOUR: {
        Value.TWO: "N",
        Value.THREE: "N",
        Value.FOUR: "N",
        Value.FIVE: "Y",
        Value.SIX: "Y",
        Value.SEVEN: "N",
        Value.EIGHT: "N",
        Value.NINE: "N",
        Value.TEN: "N",
        Value.JACK: "N",
        Value.QUEEN: "N",
        Value.KING: "N",
        Value.ACE: "N",
    },
    Value.THREE: {
        Value.TWO: "Y",
        Value.THREE: "Y",
        Value.FOUR: "Y",
        Value.FIVE: "Y",
        Value.SIX: "Y",
        Value.SEVEN: "Y",
        Value.EIGHT: "N",
        Value.NINE: "N",
        Value.TEN: "N",
        Value.JACK: "N",
        Value.QUEEN: "N",
        Value.KING: "N",
        Value.ACE: "N",
    },
    Value.TWO: {
        Value.TWO: "Y",
        Value.THREE: "Y",
        Value.FOUR: "Y",
        Value.FIVE: "Y",
        Value.SIX: "Y",
        Value.SEVEN: "Y",
        Value.EIGHT: "N",
        Value.NINE: "N",
        Value.TEN: "N",
        Value.JACK: "N",
        Value.QUEEN: "N",
        Value.KING: "N",
        Value.ACE: "N",
    },
}


if __name__ == "__main__":
    hand1 = [Card(Suite.HEARTS, Value.TEN), Card(Suite.SPADES, Value.SEVEN)]
    print(f"Hand 1 value (should be 17): {calculate_hand_value(hand1)}")

    hand2 = [Card(Suite.CLUBS, Value.ACE), Card(Suite.DIAMONDS, Value.SIX)]
    print(f"Hand 2 value (should be 17): {calculate_hand_value(hand2)}")

    hand3 = [
        Card(Suite.HEARTS, Value.ACE),
        Card(Suite.SPADES, Value.KING),
        Card(Suite.DIAMONDS, Value.TEN),
    ]
    print(f"Hand 3 value (should be 21): {calculate_hand_value(hand3)}")

    hand4 = [
        Card(Suite.CLUBS, Value.ACE),
        Card(Suite.DIAMONDS, Value.ACE),
        Card(Suite.HEARTS, Value.NINE),
    ]
    print(f"Hand 4 value (should be 21): {calculate_hand_value(hand4)}")

    hand5 = [Card(Suite.HEARTS, Value.ACE), Card(Suite.SPADES, Value.JACK)]
    print(f"Hand 5 value (should be 21): {calculate_hand_value(hand5)}")
