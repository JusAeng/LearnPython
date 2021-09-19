import random

def playing_card():
    suit=("\u2660","\u2665","\u2666","\u2663") #u=16bit U=32bit

    rank=list("A23456789")+["10"]+list("JQK")
    deck=[]
    for s in suit:
        for r in rank:
            deck.append(r+s)
    return deck
d= playing_card()
random.shuffle(d)
print(d)
p=random.sample(d,3)
print(p,type(p))