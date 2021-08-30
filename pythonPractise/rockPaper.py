import random

def play(player):
    m=("r","p","s")
    com = m[random.randrange(len(m))]
    print(f"{player} <-> com:{com} --> ",end="")
    if player == com:
        print("tie")
    elif (player=="r" and com=="s") or (player=="s" and com=="p") or (player=="p" and com=="r"):
        print("win")
    else:
        print("lose")
while True:
    player = input("[r]ock, [p]aper, [s]cissors, e[x]it :")
    if player == "x":
        break
    play(player)