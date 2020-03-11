# import libraries
import unittest                         # for the required tests
from collections import defaultdict     # to use dictionary with unknown elements
from types import SimpleNamespace       # to use the required notation

# Class for the tests
class test(unittest.TestCase):
    # testing method
    def test(self):
        # variables for the notation required
        notation = dict(WIN = "WIN", LOSS = "LOSS")
        Result = SimpleNamespace(**notation)

        # Example Cases
        self.assertTrue(PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5C 5H AC")) == Result.WIN)
        self.assertTrue(PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JC AS KC TD")) == Result.LOSS)
        self.assertTrue(PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7C JS TS 6D")) == Result.WIN)
        self.assertTrue(PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7S 5S 5D JS")) == Result.LOSS)
        self.assertTrue(PokerHand("AS AD KD 7C 3D").compare_with(PokerHand("AD AH KD 7C 4S")) == Result.LOSS)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("AC AH AS AS KS")) == Result.WIN)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JS QC KS AC")) == Result.WIN)
        self.assertTrue(PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(PokerHand("TC JS QC KS AC")) == Result.WIN)
        self.assertTrue(PokerHand("AC AH AS AS KS").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JC JS JD TH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4H 5H 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN)
        self.assertTrue(PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN)
        self.assertTrue(PokerHand("JH JC JS JD TH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.LOSS)
        self.assertTrue(PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.LOSS)
        self.assertTrue(PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)
        self.assertTrue(PokerHand("TS TH TD JH JD").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN)


# Poker Hand Class
class PokerHand:
    # constructor
    def __init__(self, cards): 
        self.hand = cards.split(" ")
        self.card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,  "T":10, "J":11, "Q":12, "K":13, "A":14}

    # Methods for each case
    def check_royal_flush(self):
        values = [i[0] for i in self.hand]
        if self.check_straight_flush() and ("A" in values):
            return True
        else:
            return False

    def check_straight_flush(self):
        if self.check_flush() and self.check_straight():
            return True
        else:
            return False

    def check_four_of_a_kind(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        for v in values: 
            value_counts[v]+=1
        max_keys = [k for k, v in value_counts.items() if v == max(value_counts.values())]
        rank_values = [self.card_order_dict[i] for i in max_keys]
        if sorted(value_counts.values()) == [1,4]:
            self.high_value = max(rank_values)
            return True
        return False

    def check_full_house(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        max_keys = [k for k, v in value_counts.items() if v == max(value_counts.values())]
        rank_values = [self.card_order_dict[i] for i in max_keys]
        if sorted(value_counts.values()) == [2,3]:
            self.high_value = max(rank_values)
            return True
        return False

    def check_flush(self):
        values = [i[0] for i in self.hand]
        suits = [i[1] for i in self.hand]
        rank_values = [self.card_order_dict[i] for i in values]
        if len(set(suits))==1:
            self.high_value = max(rank_values)
            return True
        else:
            return False

    def check_straight(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v] += 1
        rank_values = [self.card_order_dict[i] for i in values]
        value_range = max(rank_values) - min(rank_values)
        if len(set(value_counts.values())) == 1 and (value_range==4):
            self.high_value = max(rank_values)
            return True
        else: 
            #check straight with low Ace
            if set(values) == set(["A", "2", "3", "4", "5"]):
                self.high_value = 5
                return True
            return False

    def check_three_of_a_kind(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        max_keys = [k for k, v in value_counts.items() if v == max(value_counts.values())]
        rank_values = [self.card_order_dict[i] for i in max_keys]
        if set(value_counts.values()) == set([3,1]):
            self.high_value = max(rank_values)
            return True
        else:
            return False

    def check_two_pairs(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        max_keys = [k for k, v in value_counts.items() if v == max(value_counts.values())]
        rank_values = [self.card_order_dict[i] for i in max_keys]
        if sorted(value_counts.values())==[1,2,2]:
            self.high_value = max(rank_values)
            return True
        else:
            return False

    def check_one_pairs(self):
        values = [i[0] for i in self.hand]
        value_counts = defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        max_keys = [k for k, v in value_counts.items() if v == max(value_counts.values())]
        rank_values = [self.card_order_dict[i] for i in max_keys]
        if 2 in value_counts.values():
            self.high_value = max(rank_values)
            return True
        else:
            return False

    def check_high_card(self):
        values = [i[0] for i in self.hand]
        rank_values = [self.card_order_dict[i] for i in values]
        return max(rank_values)

    # Comparison of which case is
    def check_hand(self):
        values = [i[0] for i in self.hand]
        rank_values = [self.card_order_dict[i] for i in values]
        self.all_hand = sorted(rank_values, reverse=True)
        if self.check_royal_flush():
            return 10
        if self.check_straight_flush():
            return 9
        if self.check_four_of_a_kind():
            return 8
        if self.check_full_house():
            return 7
        if self.check_flush():
            return 6
        if self.check_straight():
            return 5
        if self.check_three_of_a_kind():
            return 4
        if self.check_two_pairs():
            return 3
        if self.check_one_pairs():
            return 2
        self.high_value = self.check_high_card()
        return 1
    
    # evaluation if it is a winning or losing hand
    def compare_with(self, hand_2):
        score_1 = self.check_hand()
        score_2 = hand_2.check_hand()
        if score_1>score_2:
            return "WIN"
        if score_1 == score_2:
            if(self.high_value > hand_2.high_value):
                return "WIN"
            if (self.high_value == hand_2.high_value):
                for i in range(5):
                    if(self.all_hand[i]>hand_2.all_hand[i]):
                        return "WIN"
        return "LOSS"


if __name__ == '__main__': 
    unittest.main() 