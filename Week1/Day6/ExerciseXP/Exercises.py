# Instructions
# You are given two lists. Convert them into a dictionary where the first list contains 
# the keys and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

new_dict = dict(zip(keys, values))
print(new_dict)

# Instructions
# Write a program that calculates the total cost of movie tickets for a family based on their ages.

# Family members’ ages are stored in a dictionary.
# Allow the user to input family members’ names and ages, then calculate the total ticket cost
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15
# Loop through the family dictionary to calculate the total cost.
# Print the ticket price for each family member.
# Print the total cost at the end.


total_cost = 0
family_dict = {}

user_fam = input("Enter all the names for tickets (separated by spaces})").split() #i could use a while loop here or make make an option to delete a name too
for fam in user_fam:
    age = int(input(f"Enter the age of {fam}: "))
    family_dict[fam] = age

for fam, age in family_dict.items():
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    total_cost += price
    print(f"{age}yo {fam}'s  ticket price: ${price}")

print(f"The total cost for all tickets is: ${total_cost}")

# Instructions
# Create a dictionary called brand with the provided data.
# Modify and access the dictionary as follows:
# Change the value of number_stores to 2.
# Print a sentence describing Zara’s clients using the type_of_clothes key.
# Add a new key country_creation with the value Spain.
# Check if international_competitors exists and, if so, add “Desigual” to the list.
# Delete the creation_date key.
# Print the last item in international_competitors.
# Print the major colors in the US.
# Print the number of keys in the dictionary.
# Print all keys of the dictionary.

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
brand["number_stores"] = 2

print(f"Zara clients can buy the type of clothes they need! Like: {', '.join(brand['type_of_clothes'])}.")
brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
del brand["creation_date"]

print(brand["international_competitors"][-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())

# Instructions
# You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
# Expected Results:
# 1. Create a dictionary that maps characters to their indices:
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# 2. Create a dictionary that maps indices to characters:
# {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# 3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

character2index = {}
for index, user in enumerate(users):
    character2index[user] = index
print(character2index)

index2character = {index: user for index, user in enumerate(users)}
print(index2character)

abc_users = sorted(users)
sorted_users = {user: index for index, user in enumerate(abc_users)}
print(sorted_users)

