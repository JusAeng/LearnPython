def print_string(s):
    for i in range(len(s)):
        print("{:>3}".format(i),end="")
    print()
    for i in range(-len(s),0,1):
        print("{:>3}".format(i),end="")
    print()
    for ele in s:
        print("{:>3}".format(ele),end="")
#{} = placeholder
print_string("rainbow")
s="rainbow"
print(s[-1:-5:-1])
