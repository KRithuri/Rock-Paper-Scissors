import random

while True:
    player = input("Enter a choice (R-rock, P-paper, S-scissors): ")
    possible_actions = ["r","p","s"]
    computer_choice = random.choice(possible_actions)
    print(f"\nYou chose {player}, computer chose {computer_choice}.\n")

    if player == computer_choice:
        print(f"Both players selected {player}. It's a tie!")
    elif player == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")