import random

#Dicionario que comtem as opcoes do jogo com a arte
OPTIONS = {
    0: {
        "art":'''
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        '''
    },
    1: {
        "art":'''
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        '''
    },
    2: {
        "art": '''
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        '''
    }
}

# Função que exibe a escolha do jogador ou computador
def display_choice(player, choice):
    print(f"{player} chose: {OPTIONS[choice]['art']}")

# Função que determina o vencedor do jogo    
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You Win!"
    else:
        return "You lose!"
    
# Função principal que executa o jogo
def main():
    print("Welcome to Rock, Paper, Scissors!")
    try:
        user_choice = int(input('What do you choose?'
                                    'Type 0 for Rock, 1 for paper or 2 for scissors\n'))
        if user_choice not in OPTIONS:
            raise ValueError("Invalid choice.")
    except ValueError:
        print('Invalid input!'
              'Type 0 for Rock, 1 for paper or 2 for scissors\n')
        return
    
    #Escolha do computador
    computer_choice = random.randint(0, 2)
    
    #Exibe as escolhas
    display_choice("You", user_choice)
    display_choice("Computer", computer_choice)
    
    #Determina e exibe o resultado
    result = determine_winner(user_choice, computer_choice)
    print(result) 
    
# Verifica se o script está sendo executado diretamente
if __name__=="__main__":
    main()
    