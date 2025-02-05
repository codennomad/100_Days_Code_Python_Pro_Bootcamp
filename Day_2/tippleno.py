def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_tip_percentage():
    while True:
        tip = input("Choose a tip percentage (10, 12, or 15): ")
        if tip in ["10", "12", "15"]:
            return int(tip)
        print("Please enter a valid tip: 10, 12, or 15.")

def tip_calculator():
    print("Welcome to the Tip Calculator!")
    bill = get_float_input("Enter the total bill: $ ")
    tip = get_tip_percentage()
    people = int(get_float_input("Enter the number of people splitting the bill: "))
    
    bill_with_tip = bill * (1 + tip / 100)
    total_per_person = round(bill_with_tip / people, 2)
    
    print(f"Each person should pay: ${total_per_person}")

tip_calculator()

"""
Pontos principais:
Separa a lógica em funções reutilizáveis.
Valida a entrada do usuário para o valor da conta e gorjeta.
Mais robusto e menos propenso a erros.
"""