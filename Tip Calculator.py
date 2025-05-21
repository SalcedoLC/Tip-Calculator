print("Welcome to the tip calculator!\n")

bill = float(input("Enter the total bill amount: $"))
tip = int(input("Enter a tip amount: (Do not add a '%'): "))
party_size = int(input("How many people are splitting the bill? "))

tip_amount = bill * tip / 100
total_amount = (tip_amount + bill) / party_size

print(f"Each person should pay: ${total_amount:.2f}")
