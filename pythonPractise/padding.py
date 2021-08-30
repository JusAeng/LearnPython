def demo_number():
    n=1456594
    print("{:,}".format(n))

    d=1332245.12345
    a=1243.12
    b=344.234
    print("{:20,.2f}".format(d))
    print("{:20,.2f}".format(a))
    print("{:20,.2f}".format(b)) 
def demo2():
    print("{:5}|{:15}|".format("th","Thailand"))    #{:<5} alignLegt
    print("{:>5}|{:>15}|".format("th","Thailand"))
    print("{:^5}|{:^15}|".format("th","Thailand"))   #center
demo2()