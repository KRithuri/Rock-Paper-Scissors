import random

while True:
    player = input("Enter a choice (R-rock, P-paper, S-scissors): ")
    possible_actions = ["r","p","s"]
    computer_choice = random.choice(possible_actions)