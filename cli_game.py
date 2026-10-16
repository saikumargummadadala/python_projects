#rock,paper,scissors game but using secrets module not random module
import secrets
choices="rock","paper","scissors"
player=input("enter your choice(rock,paper,scissors):").lower()
if  player in choices:
    choice = "rock", "paper", "scissors"
    comp = secrets.choice(choices)
    if comp == player:
        print(f"computer choice:{comp}")
        print(f"your choice is:{player}")
        print(" So the match  result is draw")
    elif (player == 'rock' and comp == 'scissors') or (player == 'paper' and comp == 'rock') or (
            player == 'scissors' and comp == 'paper'):
        print(f"computer choice:{comp}")
        print(f"your choice is:{player}")
        print("So the match result is you win")
    else:
        print(f"computer choice:{comp}")
        print(f"your choice is:{player}")
        print('So the match result is you lose')
else:
    print("enter the correct choice")
