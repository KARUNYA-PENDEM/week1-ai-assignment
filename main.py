import json
from datetime import datetime

# Load data from JSON file
with open("tips.json", "r") as file:
    data = json.load(file)

# Ask user name
name = input("Enter your name: ")

# Greeting
print("\nHello,", name + "!")
print("Welcome to Smart Student Assistant")

while True:
    print("\n===== MENU =====")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tip = data["study_tips"][0]
        print("\nStudy Tip:", tip)

        with open("output.txt", "a") as file:
            file.write("Study Tip: " + tip + "\n")

    elif choice == "2":
        quote = data["motivation_quotes"][0]
        print("\nMotivation Quote:", quote)

        with open("output.txt", "a") as file:
            file.write("Motivation Quote: " + quote + "\n")

    elif choice == "3":
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print("\nCurrent Date & Time:", current_time)

        with open("output.txt", "a") as file:
            file.write("Current Date & Time: " + current_time + "\n")

    elif choice == "4":
        print("\nThank you for using Smart Student Assistant!")
        break

    else:
        print("Invalid choice! Please try again.")