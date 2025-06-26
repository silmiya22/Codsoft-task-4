import random

# Available choices
options = ["rock", "paper", "scissors"]

# Initialize scores
user_score = 0
computer_score = 0

# Welcome message
print("🎮 Welcome to the Rock-Paper-Scissors Game!")
print("👉 Type 'rock', 'paper', or 'scissors' to play.")
print("👉 Type 'exit' to quit the game.\n")

def decide_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# Game loop
while True:
    user_choice = input("🧍 Your choice (rock/paper/scissors): ").lower()
    
    if user_choice == "exit":
        print("\n🏁 Final Scores:")
        print(f"🙋 You: {user_score}")
        print(f"💻 Computer: {computer_score}")
        print("👍 Thanks for playing! Goodbye.")
        break

    if user_choice not in options:
        print("❗ Invalid input. Please try again.\n")
        continue

    computer_choice = random.choice(options)
    print(f"💻 Computer chose: {computer_choice}")

    result = decide_winner(user_choice, computer_choice)

    if result == "tie":
        print("🤝 It's a tie!")
    elif result == "user":
        print("🎉 You win this round!")
        user_score += 1
    else:
        print("😞 You lose this round.")
        computer_score += 1

    print(f"📊 Score - You: {user_score} | Computer: {computer_score}\n")   

        
