def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty. Please try again.")

print("Welcome to the Band Name Generator")
city = get_non_empty_input("What's the name of the city you grew up in?\n")
pet = get_non_empty_input("What's your pet's name?\n")

band_name = f"{city.title()} {pet.title()}"
print(f"Your band name could be: {band_name}")

"""
Validação robusta com função que força o usuário a inserir algo válido.
Formatando os nomes para capitalizar corretamente com title().
"""