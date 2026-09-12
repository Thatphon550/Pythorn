import random

def checkUnique(cards):
    suit1, suit2, suit3, suit4 = False, False, False, False
    for card in cards:
        if card // 13 == 0:
            suit1 = True
        elif card // 13 == 1:
            suit2 = True
        elif card // 13 == 2:
            suit3 = True
        elif card // 13 == 3:
            suit4 = True
        
    return suit1 and suit2 and suit3 and suit4

def main():
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    deck = [x for x in range(52)]
    count = 0
    while True:
        random.shuffle(deck)
        cards = [i for i in deck[:4]]
        count += 1
        if checkUnique(cards):
            break

    for card in cards:
        print(f"{ranks[card % 13]} of {suits[card // 13]}")
    print(f"Number of picks: {count}")

main()