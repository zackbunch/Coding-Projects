def sortCards(cards):
    """ Return a sorted list of cards
    Cards are sorted based on suit first (d,s,c,h) then by rank
    If a suit not lowercase, a KeyError will be raised
    If rank is out of range, a KeyError will be raised
    """
    suits = {'d': 1, 's': 2, 'c': 3, 'h': 4}
    card_vals = {str(i):i for i in range(2, 11)} | {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return sorted(cards, key = lambda x: (suits[x[-1]], card_vals[x[:-1]]))


if __name__ == "__main__":
    cards_list = ["3c", "Js", "2d", "10h", "Kh", "8s", "Ac", "4h"]
    print(sortCards(cards_list))



  

    
    