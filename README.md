# Poker Python

Program for the comparison of 2 hands of cards using the python program

## Getting Started

The program contains a test routine, apart from the main class called PokerHand.
First use a string to enter the hand using the notation: ("KS 2H 5C JD TD") where each of the letters has the following meaning:
- A Poker hand is consists for 5 cards;
- Each card has a string with 2 (two) characters.
    - The first character is the card value and it can have the values below, ranked from lowest to highest: 
    2, 
    3, 
    4, 
    5, 
    6, 
    7, 
    8, 
    9, 
    T (10), 
    J (Jack), 
    Q (Queen), 
    K (King), 
    A (Ace), 
    - The second character is the card suit and it can assume the values: 
    S (Spades), 
    H (Hearts), 
    D (Diamonds), 
    C (Clubs)

Rules

![Poker Rules](http://www.pokersyte.com/basic/hand-rankings.jpg)

### Prerequisites

Python 3.7.6

## Running the tests

Execute the examples that are already defined.

Run
```
pytho test_py.py
```

### Using only the class

First use the class initiator and then compare with another hand.

```
poker_hand_1 = PokerHand("KS 2H 5C JD TD")
poker_hand_2 = PokerHand("9C 9H 5C 5H AC")
result = poker_hand_1.compare_with(poker_hand_2)
```