print("Welcome to the Tip Calculator!")

total_bill = float(input("What was the total bill? $"))

tip_percentage = int(input("How much tip would you like to give? 5, 10, 12, or 15? "))

num_of_people_splitting = int(input("How many people are you splitting the bill with? "))

split_per_person = (total_bill * (1 + (tip_percentage / 100))) / num_of_people_splitting

print(f"Each person should pay: ${split_per_person}")