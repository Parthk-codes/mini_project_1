import random
items = ["rock", "paper", "scissors"]

user_choice = input("Enter your choice: ")
computer_choice = random.choice(items)

print(f"User choice = {user_choice}, computer choice = {computer_choice} ")

if user_choice == computer_choice:
    print("Match Tie")
    
elif user_choice == "rock":
    if computer_choice == "paper":
        print("paper cover rock = computer win")
    elif computer_choice == "scissors":
        print("rock breaks scissors = you win")

elif user_choice == "paper":
    if computer_choice == "scissors":
        print("scissors cuts paper = computer win")
    elif computer_choice == "rock":
        print("paper covers rock = you win")

elif user_choice == "scissors":
    if computer_choice == "rock":
        print("rock breaks scissors = computer win")
    elif computer_choice == "paper":
        print("scissors cuts paper = you win")
else:
    print("Enter a valid choice from rock, paper and scissors")