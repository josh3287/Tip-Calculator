print("Welcome to the tip calculator! I hope you enjoyed your meal!")
bill = float(input("What was the total bill? "))
tip = input("What percentage tip would you like to give? 10, 15, or 20 ?")
people = int(input("How many people did you dine with? "))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill / people
print(bill_with_tip)