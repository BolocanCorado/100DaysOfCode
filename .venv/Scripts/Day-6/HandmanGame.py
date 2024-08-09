import random
import words_list





random_word = random.choice(words_list.words)
print(random_word)

word_lenght = len(random_word)
placeholder = ""
for each in range(0, word_lenght):
    placeholder += "_"
print(placeholder)

lifes = 5
game_over = False
correct_letter = []
while not game_over:
    print(f"You have {lifes} left lifes")
    guess_letter = input("Guess a letter: ").lower()
    print(f"You choose {guess_letter}")


    display = ""
    for letter in random_word:
        if letter == guess_letter:
            display += letter
            correct_letter.append(guess_letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)
    if guess_letter not in random_word:
        lifes -= 1
        if lifes == 0 :
            game_over = True
            print("Game over. Out of lifes")

    if "_" not in display:
        game_over = True
        print(f"You win. The word is {display}")





