import os

def clear_screen():
    '''Clear the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')
    
def find_highest_bidder(bidding_dictionary):
    '''Find and display the highest bidder from the auction'''
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    highest_bid = bidding_dictionary[winner]
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}.")
    
def get_bid():
    '''Prompt the use for a valid bid amount.'''
    while True:
        try:
            bid = int(input("what is your bid?: $"))
            if bid > 0:
                return bid
            else:
                print("Bid must be a positive number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric bid.")
            
def secret_aution():
    '''Run the secret aution program.'''
    print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
          ''')
    print("Welcome to the secret auction program.")
    
    auction_bids = {}
    
    while True:
        name = input("What is your name?: ").strip()
        bid = get_bid()
        auction_bids[name] = bid
        
        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
        if should_continue == "no":
            find_highest_bidder(auction_bids)
            break
        elif should_continue == "yes":
            clear_screen()
        else:
          print("Invalid response. Please type 'yes' or 'no'.")
          
if __name__=='__main__':
    secret_aution()  
        