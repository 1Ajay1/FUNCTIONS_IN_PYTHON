a=20
def outer():
             b=3
             def inner():
                          global a
                          nonlocal b
                          a=4
                          print(a+6)
                          b+=10
                          print(b+34)
             inner()
             print(b)
outer()
