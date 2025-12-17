# Instructions:
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

total_cost = 0
fam_count = int(input("How many tickets would you like yo buy?: "))
for i in range(fam_count):
    age = int(input(f"Enter the age of ticket #{i + 1}: "))
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"The ticket price for ticker #{i + 1} is: ${price}")
    total_cost += price
print(f"The total cost for all tickets is: ${total_cost}")