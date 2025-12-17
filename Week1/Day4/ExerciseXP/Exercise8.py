# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings = []
base_price = 10
topping_price = 2.5

while True: 
    topping = input("Enter a pizza topping ('quit' to finish): ")
    if topping.upper() == 'QUIT':
        break
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")      

total = base_price + (len(toppings) * topping_price)
print(f"Your toppings: {', '.join(toppings)} and it costs ${total}")
