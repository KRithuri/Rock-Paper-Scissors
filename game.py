def play_game():
    import random

    while True:
        player = input("Enter a choice (R-rock, P-paper, S-scissors): ")
        possible_actions = ["rock","paper","scissors"]
        computer_choice = random.choice(possible_actions)
        print(f"\nYou chose {player}, computer chose {computer_choice}.\n")

        if player == computer_choice:
            print(f"Both players selected {player}. It's a tie!")
        elif player == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif player == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif player == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thank you for playing!")
            break

def main():
    play_game()

main()