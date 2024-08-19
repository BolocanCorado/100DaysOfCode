import random
from game_data import data

print("Welcome to Higher or Lower Game!!")

# Format the account data intro printable format
def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_desc}, from {account_country}")

def followers(account):
    account_name = account["name"]
    account_fw = account["follower_count"]
    return (f"{account_name} has {account_fw} numbers of followers")

def compare(acc_A, acc_B):
    '''Return account with many followers'''
    accA_fw = acc_A["follower_count"]
    accB_fw = acc_B["follower_count"]
    if accA_fw > accB_fw:
        return "A"
    elif accB_fw > accA_fw:
        return "B"
    else:
        print("Both accounts has the same number of followers")

def isPlaying():
    correctGuess = True
    keepCorrectGuess = ""
    guessCount = 0
    # In order option A as winner from previous comparison
    while correctGuess:
        if keepCorrectGuess == "":
            account_a = random.choice(data)
            account_b = random.choice(data)
            if account_a == account_b:
                account_b = random.choice(data)
        elif keepCorrectGuess == "A":
            account_b = random.choice(data)
            if account_a == account_b:
                account_b = random.choice(data)
        elif keepCorrectGuess == "B":
            account_a = account_b
            account_b = random.choice(data)
            if account_a == account_b:
                account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(f"Compare B: {format_data(account_b)}")



        user_guess = input("Who has more followers between A and B? type 'A' or 'B': ").upper()
         #  Check if user guess is correct, compare followers count
        account_compare = compare(account_a, account_b)
        if user_guess == account_compare:
            if compare(account_a, account_b) == "A":
                winner = account_a
            elif compare(account_a, account_b) == "B":
                winner = account_b
            guessCount += 1
            print(f"Correct! You guess score is {guessCount}")
            keepCorrectGuess = compare(account_a, account_b)
        else:
            if compare(account_a, account_b) == "A":
                winner = account_a
            elif compare(account_a, account_b) == "B":
                winner = account_b
            print(f"Wrong! {followers(winner)} has more followers than your choice")
            print(f"Your final score is {guessCount}")
            correctGuess = False


while input("Want to play Higher/Lower game? Type 'yes' or ' no: ").lower() == "yes":
    print("\n" * 20)
    isPlaying()