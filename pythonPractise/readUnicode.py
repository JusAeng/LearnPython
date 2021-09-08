def demo_reader():  #r"C:\JusCoding\t.txt" ~roar most use in [file_name] and [recgular expression]
    with open(r"C:\JusCoding\VsCode\pythonn\learnPython\outText.txt") as f: 
        print(f.name)
        print(f.mode)               #default = r (read) ~with open("textt.txt",mode="r")
        data = f.read()
        print(data)

def demo_readUnicode():
    with open("ez.txt",mode="r",encoding="utf8") as f:
        # data = f.read()
        # print(data)
        for i, line in enumerate(f):
            print("{}. {}".format(i+1, line),end="")

def testFile():
    try:
        with open("textt.txt") as f:
            text = f.readlines()
    except FileNotFoundError:
        text=None
    for i,ele in enumerate(text):
        print(i,ele,end="")

testFile()
# demo_reader()
# demo_readUnicode()