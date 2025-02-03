import os

def clear_screen():
    """Clear the screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def choose_operation():
    """Choose a valid operation."""
    operations = {
        '+': "Addition",
        '-': "Subtraction",
        '*': "Multiplication",
        '/': "Division"
    }

    print("\nAvailable Operations:")
    for symbol, name in operations.items():
        print(f"  {symbol}: {name}")

    while True:
        operation = input("\nPick an operation: ").strip()
        if operation in operations:
            return operation
        print("Invalid operation. Please choose one of the listed operations.")

def calculate(num1, num2, operation):
    """Performs the selected operation on the two numbers."""
    try:
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None

def main():
    """Main function to run the calculator."""
    print("Welcome to the Calculator!")
    print(''' 
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |        
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|  

           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                             
    ''')
    while True:
        num1 = get_number("What's the first number? ")
        while True:
            operation = choose_operation()
            num2 = get_number("What's the next number? ")

            result = calculate(num1, num2, operation)
            if result is not None:
                print(f"\n{num1} {operation} {num2} = {result:.2f}")

            choice = input(
                f"\nType 'y' to continue calculating with {result:.2f}, "
                "or type 'n' to start a new calculation, or 'q' to quit: "
            ).strip().lower()

            if choice == "y":
                num1 = result
            elif choice == "n":
                clear_screen()
                break
            elif choice == "q":
                print("Goodbye!")
                return
            else:
                print("Invalid input. Please choose 'y', 'n', or 'q'.")

if __name__ == '__main__':
    main()
