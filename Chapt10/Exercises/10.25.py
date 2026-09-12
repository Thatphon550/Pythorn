import random

def check(cards):
    total = 0
    for card in cards:
        total += (card % 13) + 1
    return total == 24

def main():
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    deck = [x for x in range(52)]
    count = 0
    while True:
        count += 1
        random.shuffle(deck)
        if check(deck[:4]):
            break

    for card in deck[:4]:
        print(f"{ranks[card % 13]} of {suits[card // 13]}")
    print(f"Number of picks: {count}")

main()