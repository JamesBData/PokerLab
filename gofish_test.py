import unittest
import gofish

#pairs hand
hand_one = [2, 5, 6, 6, 10]
paired_card = 6
#request a pair
hand_two = [2, 4, 5, 6]
request_card = 5
hand_two.append(request_card)

hand_three = [2, 3, 4, 5]
pickup_card = 7
hand_three.append(pickup_card)

hand_four = [2, 4, 4, 5]
pickup_card_wrong = 8
hand_four.append(pickup_card_wrong)

class MyTestCase(unittest.TestCase):
    def test_pairs_hand_one(self):
        self.assertEqual((gofish.pairs(hand_one, paired_card)), 3)

    def test_pairs_hand_one(self):
        self.assertEqual((gofish.pairs(hand_two, request_card)), 3)

    def test_pairs_hand_one(self):
        self.assertEqual((gofish.pairs(hand_three, pickup_card)), 3)

    def test_pairs_hand_one(self):
        self.assertEqual((gofish.pairs(hand_one, paired_card)), 3)


if __name__ == '__main__':
    unittest.main()