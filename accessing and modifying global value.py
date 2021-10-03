a=20
def outer():
             b=14
             global a
             a=10
             print(a)
             print(b)
outer()
print(a)
