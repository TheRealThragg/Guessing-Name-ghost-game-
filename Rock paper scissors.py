import random
import time
# --- Game Start ---
print("\nWelcome to Rock Paper Scissors :)")

player_wins = 0
computer_wins = 0
choices = ["rock", "paper", "scissors"]

while True:
    # Countdown before input
    print("\nGet ready to choose!")
    for remaining in range(3, 0, -1):
        print(f"{remaining}...")
        time.sleep(1)

    # Ask for input after countdown
    player = input("\nEnter a choice (rock, paper, scissors): ").strip().lower()

    if player not in choices:
        print("❌ Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer = random.choice(choices)
    print(f"\nYou chose {player}, computer chose {computer}.")

    if player == computer:
        print(f"🤝 Both players selected {player}. It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("🪨 Rock smashes scissors. You win!")
            player_wins += 1
        else:
            print("📄 Paper covers rock. You lose.")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("📄 Paper covers rock. You win!")
            player_wins += 1
        else:
            print("✂️ Scissors cuts paper. You lose.")
            computer_wins += 1
    elif player == "scissors":
        if computer == "paper":
            print("✂️ Scissors cuts paper. You win!")
            player_wins += 1
        else:
            print("🪨 Rock smashes scissors. You lose.")
            computer_wins += 1

    print(f"\n🏆 Your Wins: {player_wins}")
    print(f"🤖 Computer Wins: {computer_wins}")

    repeat = input("\nPlay again (yes/no)? ").strip().lower()
    if repeat != "yes":
        print("\nThanks for playing")
        break
