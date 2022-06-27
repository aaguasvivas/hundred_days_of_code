print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))

percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

num_people = int(input("How many people to split the bill? "))

per_person = float((total + (total * (percentage/100))) / num_people)

print("Each person should pay: ${:0.2f}".format(per_person))
