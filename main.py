import unittest

cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')

def check_straight(card1, card2, card3):
    cards_dict = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 11, 'SQ': 12, 'SK': 13, 'SA': 14}
    cards_list = [card1, card2, card3]
    cards_list.sort(key=lambda x: cards_dict[x])
    if cards_dict[cards_list[0]] + 1 == cards_dict[cards_list[1]] and cards_dict[cards_list[1]] + 1 == cards_dict[cards_list[2]]:
        return cards_dict[cards_list[2]]
    return 0

def check_3ofa_kind(card1, card2, card3):
    if card1 == card2 == card3:
        return int(card1[1])
    return 0

def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    return 0

def play_cards(left1, left2, left3, right1, right2, right3):
    left_cards = [left1, left2, left3]
    right_cards = [right1, right2, right3]
    left_cards.sort(key=lambda x: cards.index(x))
    right_cards.sort(key=lambda x: cards.index(x))

    def is_straight_flush(cards):
        if check_straight(cards[0], cards[1], cards[2]) == 14:
            return True
        return False

    def is_three_of_a_kind(cards):
        if check_3ofa_kind(cards[0], cards[1], cards[2]) > 0:
            return True
        return False

    left_straight_flush = is_straight_flush(left_cards)
    right_straight_flush = is_straight_flush(right_cards)

    if left_straight_flush and right_straight_flush:
        return -1 if cards.index(left_cards[-1]) > cards.index(right_cards[-1]) else 1 if cards.index(left_cards[-1]) < cards.index(right_cards[-1]) else 0
    if left_straight_flush:
        return -1
    if right_straight_flush:
        return 1

    left_three_of_a_kind = is_three_of_a_kind(left_cards)
    right_three_of_a_kind = is_three_of_a_kind(right_cards)

    if left_three_of_a_kind and right_three_of_a_kind:
        return -1 if check_3ofa_kind(left_cards[0], left_cards[1], left_cards[2]) > check_3ofa_kind(right_cards[0], right_cards[1], right_cards[2]) else 1 if check_3ofa_kind(left_cards[0], left_cards[1], left_cards[2]) < check_3ofa_kind(right_cards[0], right_cards[1], right_cards[2]) else 0
    if left_three_of_a_kind:
        return -1
    if right_three_of_a_kind:
        return 1

    return 0

class TestPokerFunctions(unittest.TestCase):
    def test_check_straight(self):
        self.assertEqual(check_straight('S5', 'S6', 'S7'), 7)
        self.assertEqual(check_straight('S6', 'S5', 'S7'), 7)
        self.assertEqual(check_straight('S3', 'SQ', 'SK'), 0)

    def test_check_3ofa_kind(self):
        self.assertEqual(check_3ofa_kind('S9', 'S9', 'S9'), 9)
        self.assertEqual(check_3ofa_kind('S2', 'S4', 'S2'), 0)

    def test_check_royal_flush(self):
        self.assertEqual(check_royal_flush('SA', 'SK', 'SQ'), 14)
        self.assertEqual(check_royal_flush('S9', 'S10', 'SJ'), 0)

    def test_play_cards(self):
        self.assertEqual(play_cards('SA', 'SK', 'SQ', 'S9', 'S10', 'SJ'), 1)
        self.assertEqual(play_cards('S2', 'S4', 'S6', 'S3', 'S5', 'S7'), -1)
        self.assertEqual(play_cards('S2', 'S4', 'S6', 'SA', 'SK', 'SQ'), -1)
        self.assertEqual(play_cards('S2', 'S4', 'S6', 'S2', 'S4', 'S6'), 0)

if __name__ == "__main__":
    unittest.main()
