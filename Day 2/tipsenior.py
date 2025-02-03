def get_validated_input(prompt, valid_options=None, input_type=float):
    while True:
        user_input = input(prompt)
        try:
            value = input_type(user_input)
            if valid_options and str(value) not in valid_options:
                raise ValueError("Invalid choice.")
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {' or '.join(valid_options) if valid_options else 'value'}.")

def calculate_tip(bill, tip_percentage, num_people):
    bill_with_tip = bill * (1 + tip_percentage / 100)
    return round(bill_with_tip / num_people, 2)

def main():
    print("Welcome to the Tip Calculator!")
    bill = get_validated_input("Enter the total bill: $ ", input_type=float)
    tip_percentage = get_validated_input("Choose a tip percentage (10, 12, 15): ", ["10", "12", "15"], input_type=int)
    num_people = get_validated_input("How many people to split the bill? ", input_type=int)
    
    amount_per_person = calculate_tip(bill, tip_percentage, num_people)
    print(f"Each person should pay: ${amount_per_person}")

if __name__ == "__main__":
    main()

"""
Pontos principais:
Funções reutilizáveis e genéricas para validação de entradas.
Entrada flexível e robusta, evitando travamentos com dados inválidos.
Melhora na separação de lógica para facilidade de manutenção.
Uso de estrutura condicional principal para permitir expansão futura ou integração com outros sistemas.
"""