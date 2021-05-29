import random


def gamewin(a,b):
    if a==b:
        return None
    elif a=='s':
        if b=='p':
            return True
        elif b=='sc':
            return False
        else:
            print("Enter a valid input")
    elif a=='p':
        if b=='s':
            return False
        elif b=='sc':
            return True
        else:
            print("Enter a valid input")
    elif a=='sc':
        if b=='s':
            return True
        elif b=='p':
            return False
        else:
            print("Enter a valid input")
        

compchoose=random.randint(1,2)
if compchoose == 1:
    comp = "s"
elif compchoose == 2:
    comp = 'p'
else:
    comp = 'sc'

player=input("Your turn : Choose from Stone(s) paper(p) scissor(sc)")

print("coomputer chose "+ comp)
print("you chose "+ player)
win = gamewin(comp , player)
if win == None:
    print("The game is a tie")
elif win:
    print("You won")
else:
    print("You Lost")
