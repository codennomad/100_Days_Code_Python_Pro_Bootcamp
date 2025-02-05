import random
import string

# Function to get a valid number from the user
def get_valid_number(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("The number cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input. Please try again. Error: {e}")
            
# Function to generate the password
def generate_password(nr_letters: int, nr_symbols: int, nr_numbers: int) -> str:
    letters = string.ascii_lowercase
    symbols = string.punctuation
    numbers = string.digits
    
    password_list = [
        random.choice(letters) for _ in range(nr_letters)
    ] + [
        random.choice(symbols) for _ in range(nr_symbols)
    ] + [
        random.choice(numbers) for _ in range(nr_numbers)
    ]
    
    # Shuffle to make the password more random
    random.shuffle(password_list)
    
    # Convert the list to a string
    return ''.join(password_list)

# Main function
def main():
    print("Welcome to the PyPassword Generator!")
    
    # Get valid numbers for each character type in the password
    nr_letters = get_valid_number(f"How many letters would you like in your password?\n")
    nr_symbols = get_valid_number(f"How many symbols would you like?\n")
    nr_numbers = get_valid_number(f"How many numbers would you like?\n")
    
    # Generate and display the password
    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print(f"You generated password is: {password}")
    
if __name__ == '__main__':
    main()