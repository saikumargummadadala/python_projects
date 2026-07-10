import random
comp=['rock','paper','scissors']
comp_choice=random.choice(comp)
user=input("choose one (rock,paper,scissors:)").lower()
if comp_choice==user:
    print(f"computer choice:{comp_choice}")
    print(f"your choice is:{user}")
    print(" So the match  result is draw")
elif (user == 'rock' and comp_choice == 'scissors') or(user == 'paper' and comp_choice == 'rock') or (user == 'scissors' and comp_choice == 'paper'):
    print(f"computer choice:{comp_choice}")
    print(f"your choice is:{user}")
    print("So the match result is you win")
else:
     print(f"computer choice:{comp_choice}")
     print(f"your choice is:{user}")
     print('So the match result is you lose')
    