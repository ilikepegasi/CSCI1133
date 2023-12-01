def rank_suit_count(cards: list[str]) -> list[dict]:
    rank_freq = {}
    suit_freq = {}
    for card in cards:
        if card[0] in rank_freq:
            rank_freq[card[0]] += 1
        else:
            rank_freq[card[0]] = 1
        if card[1] in suit_freq:
            suit_freq[card[1]] += 1
        else:
            suit_freq[card[1]] = 1
    return [rank_freq, suit_freq]

def poker_hand(cards:list[str]) -> str:
    rank_nums = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 1}
    counted_cards = rank_suit_count(cards)
    if 5 in counted_cards[1].values():
        full_house_check = []
        for rank in counted_cards[0]:
            is_face = False
            for key in rank_nums:
                if key == rank:
                    is_face = True
                    full_house_check.append(rank_nums[rank])
            if not is_face:
                full_house_check.append(int(rank))
        for i, ele in enumerate(full_house_check):
            full_house_check[i] -= min(full_house_check)
        if full_house_check == list(range(0, 5)):
            return("Full House")

    
    


def main():
    print(rank_suit_count(['AD','AD','2D','TD','TD']))
    print(poker_hand(['8D', '9D', 'TD', 'JD', 'QD']))

if __name__ == "__main__":
    main()