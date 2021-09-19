#set not contain duplicate element ,dont care order

example=set()
example.add(42)
example.add(False)
example.add(3.12)
print(example,len(example))

example2=set({1,2,42})
example2.remove(1)
print(example2)
# print(example2-example)

a=example.union(example2)
print(a)
for ele in a:
    print(ele)