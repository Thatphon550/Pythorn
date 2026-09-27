import random

def main():
    ranking = ["assistant", "associate", "full"]
    outfile = open("Salary.txt", "w")
    for i in range(1, 1001):
        rank_index = random.randint(0, len(ranking) - 1)
        income = ""
        if rank_index == 0:
            income += f"{random.randint(50000, 80000)}"
        elif rank_index == 1:
            income += f"{random.randint(60000, 110000)}"
        elif rank_index == 2:
            income += f"{random.randint(75000, 130000)}"

        cents = random.randint(0, 99)
        income += f".0{cents}" if cents <= 9 else f".{cents}"
        outfile.write(f"FirstName{i} LastName{i} {ranking[rank_index]} {income}\n")
    outfile.close()

main()
