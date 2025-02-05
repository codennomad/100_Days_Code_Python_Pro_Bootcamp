import random
import os

def clear_screen():
    '''Clear the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

def get_choose(prompt, valid_inputs=None):
    '''Gets and validates user input
    
    valid_inputs (list, optional): List of valid inputs. If None, accepts any input.
    '''
    while True:
        try:
            return input(prompt)
        except ValueError:
            print("Invalid input. Type 'y' to get another card, type 'n' to pass: ").strip().lower()
                      
def draw_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(hand):
    '''Draws a random card. Cards are value 2-11(11 representing Ace)'''
    score = sum(hand)
    if 11 in hand and score > 21:
        score -= 10
    return score

def display_hands(player_hand, computer_hand, show_computer_card = False):
    '''Display the hands of the player and the computer
    
     Args:
        player_hand (list): Player's hand.
        computer_hand (list): Computer's hand.
        show_computer_card (bool): Whether to reveal all computer's cards.
    '''
    print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
    if show_computer_card:
        print(f"Computer's cards: {computer_hand}, score: {calculate_score(computer_hand)}")
    else:
        print(f"Computer's first card: {computer_hand[0]}")
        
def play_blackjack():
    '''Run a game '''
    clear_screen()
    print("Welcome to Blackjack!")
    print ('''
           
88          88                       88        88                       88                 
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                 
           ''')
    
    #Initial hand
    player_hand = [draw_card(), draw_card()]
    computer_hand = [draw_card(), draw_card()]
    
    gamer_over = False
    while not gamer_over:
        display_hands(player_hand, computer_hand)
        
        #check for player's Blackjack or bust
        player_score = calculate_score(player_hand)
        if player_score == 21:
            print("Blackjack! You win!")
            return
        elif player_score > 21:
            print("You went over 21! Computer wins.")
            return
        
        #Ask if player wants another card
        choice = get_choose("Type 'y' to get another card or 'n' to pass: ", valid_inputs=['y', 'n'])
        if choice == "y":
            player_hand.append(draw_card())
        else:
            gamer_over = True
            
    #computer's turn
    while calculate_score(computer_hand) < 17:
        computer_hand.append(draw_card())
        
    #display final hands
    display_hands(player_hand, computer_hand, show_computer_card=True)
    
    #determine the winner
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)
    
    if computer_score > 21 or player_score > computer_score:
        print("Congratulations, you win!")
    elif player_score == computer_score:
           print("It's a draw!")
    else:
         print("Computer wins.")
                     
def main():
    '''Main function to initiate the game'''
    while True:
        play = get_choose("Do you want to play a game of Blackjack? Type 'y' or 'n': ", valid_inputs=['y', 'n'])
        if play == "y":
            play_blackjack()
        else:
            print("Thanks for playing! Goodbye.")
            break
        
if __name__ == '__main__':
    main()
    