import random

items_list = ["Rock", "Paper", "Scissor"]

my_choice = input("Enter your move (Rock, Paper, Scissor): ")
bot_choice = random.choice(items_list)

print(f"My choice = {my_choice}, Bot choice = {bot_choice}")

if my_choice == bot_choice:
    print("Game Tie")

elif my_choice == "Rock" and bot_choice == "Paper":
    print("Paper wins")

elif my_choice == "Rock" and bot_choice == "Scissor":
    print("Rock wins")

elif my_choice == "Paper" and bot_choice == "Rock":
    print("Paper wins")

elif my_choice == "Paper" and bot_choice == "Scissor":
    print("Scissor wins")

elif my_choice == "Scissor" and bot_choice == "Rock":
    print("Rock wins")

elif my_choice == "Scissor" and bot_choice == "Paper":
    print("Scissor wins")

else:
    print("Enter a valid word")

print("Thank you for playing")