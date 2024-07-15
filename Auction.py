bidders = {}

name = input("Enter name: ")
bid = int(input("Enter your bid: "))
others = input("Are there other buyers? ").lower()

while others != "no":
    bidders[name] = bid
    name = input("Enter name: ")
    bid = int(input("Enter your bid: "))
    others = input("Are there other buyers? ").lower()
    
bidders[name] = bid

print(bidders)

bid_amounts = [v for v in bidders.values()]

print(bid_amounts)

max_bid = max(bid_amounts)

for k in bidders:
    if bidders[k] == max_bid:
        print(f"Max bid is {bidders[k]} by {k}")
        
        