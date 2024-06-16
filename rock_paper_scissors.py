import random

user_wins = 0
computer_wins = 0
#Stores rock paper scissors as elements in a list for simplicity in later code
options = ["rock", 'paper', 'scissors']
print("Welcome to Rock, Paper, Scissors!")
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit/end game: ").lower()
    #Breaks out of while loop

    if user_input == 'q':
        break
    #Using list, checks if user_input is equal to either of the elements 
    if user_input not in options:
        #Will reask them to type rock/paper/scissors from above
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f"Computer Picked: {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        continue
#Since all 3 victory cases are accounted for, we can simply use a else to account for all cases where the computer wins
    else:
        print("Computer Wins!")
        computer_wins += 1
        continue
    
print("\nGame Over, Results are below: \n")
#Prints final result of who wins overall
if user_wins > computer_wins:
    print("Well played, you beat the computer!")
elif computer_wins > user_wins:
    print("You lost, better luck next time!")
else:
    print("You both tied!")
#Next two if statements are to fix grammar errors when printing final # of wins for computer and user
if user_wins == 0 or user_wins >= 2:
    print(f"You won {user_wins} times!")
else:
    print(f"You won {user_wins} time!")

if computer_wins == 0 or computer_wins >= 2:
    print(f"Computer won {computer_wins} times!")
else:
    print(f"Computer won {computer_wins} time!")