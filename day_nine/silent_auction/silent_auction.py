import os
from art import logo

end_of_bid = False
bidders = {}

print(logo)
print("Welcome to the secret auction program.")

while not end_of_bid:

    # User input
    bidder = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    # Add to dict
    bidders[bidder] = bid

    # Check end of program
    check_end_of_bids = input(
        "Are there any other bidders? Type 'yes' or 'no': ").lower()

    if check_end_of_bids == 'no':
        end_of_bid = True

    os.system('clear')

# Check max
max_bidder = max(bidders, key=bidders.get)
print(f"The winner is {max_bidder} with a bid of ${bidders[max_bidder]}.")
