print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give: 10, 12, 15?\n"))
people = int(input("How many people to split the bill?\n"))
bill_with_tip = bill + (bill * tip/100)
Pay_Per_person = bill_with_tip / people
print(f"EACH PERSON SHOULD PAY: ${round(Pay_Per_person,  2)}")

