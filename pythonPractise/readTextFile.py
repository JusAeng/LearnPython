def demo_read():
    a=open("textt.txt")
    data=a.read()
    print(data)
    a.close()
def demo_readline():
    a=open("textt.txt")
    data=a.readline()
    a.close()
    print(data)
    data2=a.readline()
    a.close()
    print(data2)
def demo_readlines():
    a=open("textt.txt")
    data=a.readlines()
    print(data)
    a.close()
def demo_readlines2():
    f=open("textt.txt")
    for line in f:
        print(line.capitalize(),end="")
    f.close()


demo_readlines()