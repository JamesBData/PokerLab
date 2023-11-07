import math

cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')

def check_straight(card1, card2, card3):
    cards_dict = {'S2': 2, 'S3': 3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8, 'S9': 9, 'S10': 10, 'SJ': 11, 'SQ': 12, 'SK': 13, 'SA': 14}
    cards_list = [card1, card2, card3]
    cards_list.sort(key=lambda x: cards_dict[x])
    return cards_dict[cards_list[2]] if cards_dict[cards_list[0]] + 1 == cards_dict[cards_list[1]] and cards_dict[cards_list[1]] + 1 == cards_dict[cards_list[2]] else 0

def check_3ofa_kind(card1, card2, card3):
    return int(card1[1]) if card1 == card2 == card3 else 0

def check_royal_flush(card1, card2, card3):
    return 14 if check_straight(card1, card2, card3) == 14 else 0

def play_cards(left1, left2, left3, right1, right2, right3):
    left_cards = [left1, left2, left3]
    right_cards = [right1, right2, right3]
    left_cards.sort(key=lambda x: cards.index(x))
    right_cards.sort(key=lambda x: cards.index(x))

    def is_straight_flush(cards):
        return check_straight(cards[0], cards[1], cards[2]) == 14

    def is_three_of_a_kind(cards):
        return check_3ofa_kind(cards[0], cards[1], cards[2]) > 0

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

left1 = 'SA'
left2 = 'SK'
left3 = 'SQ'
right1 = 'S9'
right2 = 'S10'
right3 = 'SJ'

result = play_cards(left1, left2, left3, right1, right2, right3)
if result == -1:
    print("Left player wins!")
elif result == 1:
    print("Right player wins!")
else:
    print("It's a draw!")