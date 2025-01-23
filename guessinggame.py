import random

secret_number = random.randint(1, 20)
print("I am thinking of number between 1 and 20")

for i in range(1, 7):
    print("Take a guess.")
    guess = int(input())
    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print("You guessed the right number! It took " + str(guess) + " Times" )
