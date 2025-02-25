import random

word_list = ["apple", "pinapple", "lemon"]

lives= 6

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for letter_position in range(word_length):
    placeholder += "_"
print(placeholder)

gameover = False
correct_letters = []

while not gameover:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letters in chosen_word:
        if letters == guess:
            display += letters
            correct_letters.append(guess)
        elif letters in correct_letters:
            display += letters
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            gameover = True
            print("You Lose!")

    if "_" not in display:
        gameover = True
        print("You win!")