import random

user_wins = 0
computer_wins = 0

options = ["rock", 'paper', 'scissors']

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
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


print("Goodbye")
