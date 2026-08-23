import random 

randomNum = random.randint(1, 100)

count = 0

print("========================")
print("    GUESS THE NUMBER")
print("========================")
print("\nI'm thinking of a number between 0 and 100!")

guess = int(input("Enter your guess: "))

while guess != randomNum:
    count += 1
    if guess > randomNum:
        print("Too high!")
    elif guess < randomNum:
        print("Too low!")
    elif gues == randomNum:
        break
    guess = int(input("Enter your guess: "))
    
print("🎉 Correct!")
print(f"You guessed it in {count} attempts!")