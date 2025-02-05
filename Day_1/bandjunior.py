def get_input(prompt):
    return input(prompt).strip()

print("Welcome to the Band Name Generator")
city = get_input("What's the name of the city you grew up in?\n")
pet = get_input("What's your pet's name?\n")

if city and pet:
    print(f"Your band name could be: {city} {pet}")
else:
    print("Please enter valid names for both city and pet!")

"""
Melhor legibilidade com função para entrada.
Validação básica para garantir que as entradas não sejam vazias.

"""