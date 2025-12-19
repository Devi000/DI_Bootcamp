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