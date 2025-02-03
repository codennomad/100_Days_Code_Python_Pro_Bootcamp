def get_input_with_validation(prompt, allow_empty=False):
    while True:
        user_input = input(prompt).strip()
        if allow_empty or user_input:
            return user_input
        print("Please enter a valid name.")

def generate_band_name():
    print("Welcome to the Band Name Generator!")
    city = get_input_with_validation("What's the name of the city you grew up in?\n")
    pet = get_input_with_validation("What's your pet's name?\n")
    band_name = f"{city.title()} {pet.title()}"
    print(f"\n🎵 Your band name could be: '{band_name}' 🎸")

if __name__ == "__main__":
    generate_band_name()

"""
Design escalável com funções genéricas.
Melhor experiência do usuário, com validação robusta e mensagens amigáveis.
Organização para reuso e fácil integração com futuras melhorias.

"""