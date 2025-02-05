print("Welcome to the Tip calculator!")
bill = float(input("What was the total bill ? $ "))
tip = int(input("How much tip would you like to given? 10, 12 or 15? "))
people = int(input("How many people split the bill? "))

bill_with_tip = tip / 100 * bill + bill
total_per_person = bill_with_tip / people
final_amount = round(total_per_person, 2)

print(f"Each person should pay: $ {final_amount}")