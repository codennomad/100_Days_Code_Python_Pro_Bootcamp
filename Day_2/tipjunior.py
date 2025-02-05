def calculate_tip():
    print("Welcome to the Tip Calculator!")
    
    bill = float(input("Enter the total bill amount: $ "))
    tip = int(input("Choose a tip percentage (10, 12, 15):"))
    people = int(input("Enter the number of people splitting the bill:"))
    
    if tip not in [10, 12, 15]:
        print("Invalid tip percentage. Defaulting to 10%.")
        tip = 10
        
    bill_with_tip = bill * (1 + tip / 100)
    total_per_person = round (bill_with_tip / people, 2)
    
    print(f"Each person should pay: ${total_per_person}")

calculate_tip()

"""
Pontos principais:
Organiza o código em uma função para reutilização.
Verifica se a gorjeta escolhida é válida.
Mais legível e fácil de entender.
"""