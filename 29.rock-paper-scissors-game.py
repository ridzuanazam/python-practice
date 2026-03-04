import random

options = ("rock", "paper", "scissors")
player = None
player_score = 0
computer = random.choice(options)
computer_score = 0
is_running = True

while is_running: 

    player = input("Enter a choice (rock, paper, scissors): ").lower()

    if player in options:
        print(f"Player   : {player}")
        print(f"Computer : {computer}")
        print("-----------------")
        if  (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
            print("Player win!")
            print("-----------------")
            player_score += 1
            print(f"Player Score   : {player_score}\nComputer Score : {computer_score}")
            player = None
            continue
        elif (player == "rock" and computer == "rock") or (player == "paper" and computer == "paper") or (player == "scissors" and computer == "scissors"):
            print("Player and Computer Draw!")
            print("-----------------")
            print(f"Player Score   : {player_score}\nComputer Score : {computer_score}")
        else:
            print("Computer win!")
            print("-----------------")
            computer_score += 1
            print(f"Player Score   : {player_score}\nComputer Score : {computer_score}")
            computer = random.choice(options)

        if player_score == 3:
            print("Player is THE WINNER")
            is_running = False
        if computer_score == 3:
            print("Computer is THE WINNER")
            is_running = False
    else:
        print("INVALID INPUT! TRY AGAIN.")
    
   