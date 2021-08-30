def alpha(a,b): #dynamic type
    return a+b

def beta(a:int,b:str): #type hint1 (not static type) //can build-in function
    print(a,b.upper())

class Person:
    def __init__(self,fname):
        self.fname=fname
    def epsilon(self):
        print("hello")

def delta(a:Person,b):
    a.epsilon()

def bar(a,b) -> str: #type hint2 //to tell what return type
    return a+b

if __name__ == '__main__':
    beta(1,"eiei")
    beta("eiei","eiei") #a don't need to be int
    te1=Person("jus")
    delta(te1,2)
    alpha()