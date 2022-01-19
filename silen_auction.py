from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

def winner():
  offer = 0
  for bids in bidder:
   competitor= bidder[bids]
  if competitor > offer :
    offer += competitor

bidder = {}



def new_bidder(new_name, new_price, ):
  bidder[new_name]= new_price
  clear()
more_bidders= "yes"

while more_bidders == "yes":

 new_bidder( (input("What is your name?\n")),(input("What it your bid?\n$")) ,
 )
 more_bidders= (input("Are there any other bidders? Type 'yes' or 'no'\n"))
 clear()
if more_bidders == "no":
   more_bidders= "no"
   offer = 0
for bids in bidder:
   competitor= int(bidder[bids])
if competitor > offer :
    offer += competitor


print(f"The winner is {bids} whit a bid of $ {offer}")

print(f"All offers where {bidder} :")