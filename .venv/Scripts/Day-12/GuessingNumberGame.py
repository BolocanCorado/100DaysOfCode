from random import randint

def easyMode():
    attempts = 10
    return attempts

def hardMode():
    attempts = 5
    return attempts

play_again = True
def is_playing():
    print("Welcome to guessing number game!")
    print("I'm tinking at a number between 1 and 100")

    answer = randint(1, 100)
    print(f"PS: I am thinking at number {answer}")
    is_over = False


    mode = 0
    user_mode_correct = True
    while user_mode_correct:
        user_mode = input("Choose the difficulty of the game, 'easy' or 'hard': ").lower()
        if user_mode == "easy":
            print("You have choose easy mode. You have 10 attempts")
            user_mode_correct = False
        elif user_mode == "hard":
            print("You have choose hard mode. You have 5 attempts")
            user_mode_correct = False
        else:
            print("Only 'easy' or 'hard' options are available")

    if user_mode == "easy":
        mode = easyMode()
    elif user_mode == "hard":
        mode = hardMode()

    while not is_over:
        user_numer = int(input("Choose a number: "))
        if answer == user_numer:
            print(f"You win. You found the number. {answer} was the number that should guess")
            is_over = True
        elif mode == 1:
            is_over = True
            print("Game Over! No attempts available")
        elif mode != 1  and answer != user_numer:
            
            if answer > user_numer:
                mode -= 1
                print("Too low")
                print(f"You have {mode} left")
            elif answer < user_numer:
                mode -= 1
                print("Too high")
                print(f"You have {mode} left")

while play_again:
    wantPlay = input("Do you want to play Guessing Number Game? 'yes' or 'no': ")
    if wantPlay == "yes":
        print("\n" * 20)
        is_playing()
    else:
        play_again = False








