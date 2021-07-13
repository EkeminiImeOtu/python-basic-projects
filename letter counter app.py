#letter counter app

print("Welcome to the Letter Counter App")

#Get user input

name = input("\nWhat is your name: ").title().strip()
print("Hello, " + name + "!")

print("I will count the number of times that a specific letter occurs in a message you will input.")

message=input("\nPlease enter a message: ")
letter=input("Which letter would you want to be counted? ")


#standardize to lower case.
message=message.lower()
letter =letter.lower()


#Get the count and display results.
letter_count = message.count(letter)
print("\n" + name + ", your message has " + str(letter_count) + " " + letter + "'s in it.")

