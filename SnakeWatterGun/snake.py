# Snake Water Gun Game
import random

user = int(input("Enter 0 snake , 1 for water or 2 Gun:\n"))

comp = random.randint(0, 2)

print("User: ", user)
print("Comp: ", comp)

def run_game(comp, user):
    if comp == user:
        return 0
    
    if (user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0):
        return 1
    else:
        return -1

value = run_game(comp, user)
if value == 0:
    print("Game Draw!")
elif value == 1:
    print("You Won")
else:
    print("You Loose")