print("Welcome to the Tip Calculator!")

total_bill = float(input("What is the total bill? $"))
tip = int(input("What percentage tip would you like to give- 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

bill_per_person = (tip / 100 * total_bill + total_bill)/no_of_people
final_amount=f"{bill_per_person:.2f}"

print(f"Each person should pay : ${final_amount}")