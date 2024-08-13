import random


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, the opponent has Blackjack!"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    user_cards = []
    computer_cards =[]
    computer_score = -1
    user_score = -1

    is_game_over = False
    #Append first two random cards in user_cards and computer_cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        #Calculate user and computer score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        #Show first two cards of user and first card of computer
        print(f"Your cards : {user_cards} and the score is {user_score}")
        print(f"Computer first card: {computer_cards[0]}")
        #checking if user or computer has blackjack or user score over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        #Asking for another card for user
        else:
            anotherCard = input("Do you want another card?: 'yes', or 'no' ").lower()
        #If another card is wanted, it is added to user_cards and sum of user_cards
            if anotherCard == "yes":
                user_cards.append(deal_card())
        # If not, game is over, first two cards of user will be compared. Computer draw cards until while loop is done
            else:
                is_game_over = True
    # Computer is drawing cards until condition is ment
    while computer_score != 0 and computer_score < 17:
        #After one random card, it will be added to computer_cards and cards will be added to the computer_score
        #If computer_score is over 17, loop will end
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand {user_cards}, final score {user_score}")
    print(f"Computer's final hand {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want another game? Type 'yes' or 'no': ") == "yes":
    print("\n" * 20)
    play_game()