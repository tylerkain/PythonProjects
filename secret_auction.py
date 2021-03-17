
is_bidding = False


auction_bids={}
def highest_bid(bidder_record):
  winning_bid = 0

  for bidder in bidder_record:
    bid_amount = bidder_record[bidder]
    if bid_amount >winning_bid:
      winning_bid = bid
      
  print(winning_bid)

while not is_bidding:
  name = input("whats your name: ")
  bid = int(input("whats your bid: "))
  auction_bids[name]= bid
  num_of_bidders = input("are there other bidders y/n: ").lower()
  if num_of_bidders == "n":
    is_bidding = True
    highest_bid(auction_bids)
  elif num_of_bidders == "y":
    clear()
