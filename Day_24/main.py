# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
# with open("new_file.txt", "w") as file:
#     file.write("\nNew text.")
PLACEHOLDER = "[name]"

with open("./Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    
with open("./Letters/starrting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./ReadyToSend/letter_for_{stripped_name}.docx", "w") as completed_letter:
            completed_letter.write(new_letter)