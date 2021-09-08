def alpha():
    oceans=["Pacific","Atlantic","Indian","Southen","Arctic"]

    with open("ocean.txt","w") as f:    #if file not exist python will create,if it exist python will overwrited
        for ocean in oceans:
            # f.write(ocean)
            # f.write("\n")
            print(ocean,file=f)
def beta(): #"a"mode ~created file if not exist ,but if exist python will append your text
    with open("ocean.txt","a") as f:
        print("="*20,file=f)
        print("These are the 5 oceans.",file=f)

# alpha()
beta()