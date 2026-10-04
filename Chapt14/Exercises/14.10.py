import random

states = {"Alabama": "a"}

state = random.choice(list(states.keys()))
count = 0
while True:
    answer = input(f"What is the capital of {state}: ").strip()
    if answer == states[state]:
        break
    else:
        count += 1
print(f"Correct: You missed {count} time(s)")
