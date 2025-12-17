# Instructions:
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
while True:
    username = input("Enter your name: ")
    if username.isdigit() or len(username) < 3:
        print("Please enter a name with at least 3 letters and no digits.")
    else:
        print("thank you")
        break
