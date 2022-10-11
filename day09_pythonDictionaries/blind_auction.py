from art import logo

print(logo)
print("Welcome to the blind auction program")


def find_highest_bidder(bid_values):
    highest_bid = 0
    winner = ""
    for bidder in bid_values:
        if bid_values[bidder] > highest_bid:
            highest_bid = bid_values[bidder]
            winner = bidder
    print(f"The winner is {winner} with bid of {highest_bid}")


bids = {}
bidding_finish = False
while not bidding_finish:
    print("----------------------------")
    name = input("What is your name ?: ")
    bid = float(input(f"What is your bid price {name}?: "))
    bids[name] = bid
    is_continue = input("Are there any other bidders ? Type 'yes' or 'no'").lower()
    if is_continue == "no":
        bidding_finish = True
print("----------------------------")
print(bids)

print("----------------------------")
find_highest_bidder(bids)
