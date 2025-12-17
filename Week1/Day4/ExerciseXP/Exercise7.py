# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

fav_fruits = input("Enter your favorite fruits, separated by spaces: ").split()
user_fruit = input("Enter the name of any fruit: ")
if user_fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
