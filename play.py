# import random module
import random

# print multiline instruction
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    # take the input from user
    choice=int(input("Enter your choice :"))
    # looping until user enter invalid input
    while choice > 3 or choice <1:
      choice=int(input('Enter a valid choice please!'))

    # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name= 'Rock'
    elif choice == 2:
        choice_name= 'Paper'
    else:
        choice_name= 'Scissors'

       # print user choice
    print('User choice is \n',choice_name)
    print('Now its Computers Turn....')

    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1,3)

    # looping until comp_choice value
    # is equal to the choice value
    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'rocK'
    elif comp_choice == 2:
        comp_choice_name = 'papeR'
    else:
        comp_choice_name = 'scissoR'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name,'Vs',comp_choice_name)

    # we need to check of a draw
    if choice == comp_choice:
        print('Its a Draw',end="")
        result="DRAW"