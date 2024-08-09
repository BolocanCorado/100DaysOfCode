print("Welcome to Trasure island!!")
print("Your mission is to find out the trasure after complete the quest")
name = input("What is your name? ")

first_step = input("You are in front of two doors. Where do you want to go? Type 'left' or 'right'").lower()
if first_step == "left":
    second_step = input("In front of you is a lake. Do you 'swim' or 'wait' a boat? Type 'swim' or 'wait'").lower()
    if second_step == "wait":
        third_step = input("The boat transfer you in front of three doors. Which one do you prefer? Type 'yellow', 'blue', 'red'").lower
        if third_step == "yellow":
            print(name + " You win the tresure!!!")
        elif third_step == "blue" or third_step == "red":
            print(name + " You lose the tresure!!!")
        else:
            print("You choose a door that doesn't exist.")
    else:
        print("The lake is full of sharks.")
else:
    print("The game is over")

