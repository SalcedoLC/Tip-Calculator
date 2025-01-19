print("Welcome to the Tip Calculator!\n")
bill = float(input("What was the total bill? \n"))
tip = int(input("What percentage tip would you like to leave? ex. 10, 12, 15 \n"))
amount_of_people = int(input("How many people will be splitting the bill? \n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / amount_of_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay {final_amount}")