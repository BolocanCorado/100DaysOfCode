def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"Winner is {winner} having {highest_bid}$ bidded")



print("Here is the Secret Action")
print("\n" * 100)

still_bids = True
bids = {}
while still_bids:

    name = input("What is your name? \n")
    name_duplicated = True
    while name_duplicated:
        if name in bids:
            print("Name already exists. Add another one")
            name = input("What is your name? \n")
        else:
            name_duplicated = False
    price = int(input("What is your bid?: $\n"))
    bids[name] = price
    should_continuie = input("Are there any other biddes? Type 'yes' or 'no': ")
    #There is a problem, does not exit from the loop even with 'yes' or 'no' if i have .lower
    #yesno = True
    #while yesno:
    #    if should_continuie != "yes":
    #        print("Only 'yes' or 'no' is accepted")
    #        should_continuie = input("Are there any other biddes? Type 'yes' or 'no': ").lower
    #    elif should_continuie != "no":
    #        print("Only 'yes' or 'no' is accepted")
    #        should_continuie = input("Are there any other biddes? Type 'yes' or 'no': ").lower
    #    else:
    #        yesno = False
    if should_continuie == "no":
        still_bids = False
        find_highest_bidder(bids)
        print(bids)
    elif should_continuie == "yes":
        print("\n" * 100)




