import random

print("Welcome to the Rock Paper Scissors Game!")


options = ["rock", "paper", "scissors"]


user_score = 0
computer_score = 0

while True:
    print("\nChoose any one: rock / paper / scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in options:
        print("Invalid input! Please type rock, paper or scissors.")
        continue

    computer_choice = random.choice(options)
    print("Computer chose:", computer_choice)

    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You won this round!")
        user_score += 1
    else:
        print("Computer won this round!")
        computer_score += 1

    
    print(f"Your score: {user_score} | Computer score: {computer_score}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nFinal Results:")
        print(f"You: {user_score} | Computer: {computer_score}")
        if user_score > computer_score:
            print("You are the overall winner! 🎉")
        elif computer_score > user_score:
            print("Computer wins the game! 🤖")
        else:
            print("The game ended in a tie!")
        print("Thanks for playing!")
        break