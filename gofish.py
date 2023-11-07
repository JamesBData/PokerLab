

def pairs(hand_list, remove_card):
    c = hand_list.count(remove_card)
    for card in range(c):
        hand_list.remove(remove_card)
    return len(hand_list)

card_list = [0,1,2,3]
removed_card = 2
print(pairs(card_list, removed_card))

