print("Welcome to the tip calculator!")
bill_total = float(input("What was the total bill?:\n "))
tip_percentage = float(input("How much tip would you like to give? 10, 12 or 15?:\n "))
accepted_percentage = [10,12,15]
while tip_percentage not in accepted_percentage:
        tip_percentage = float(input("INCORRECT INPUT! Choose one of the following values: 10, 12 or 15?:\n "))
final_tip = bill_total * (tip_percentage / 100)
split_counter = float(input("How many people to split the bill?:\n "))
final_total = round((bill_total + final_tip) / split_counter, 2)

print(f"Your final total per person is {final_total}")
