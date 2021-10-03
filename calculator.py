def calc():
             print("If you want to exist then entered space")
             while True:
                          a,st,b=int(input()),input(),int(input())
                          if st=='+':
                                       c=a+b
                          elif st=='-':
                                       c=a-b
                          elif st=='*':
                                       c=a*b
                          elif st=='/':
                                       c=a/b
                          elif st=='%':
                                       c=a%b
                          elif st==' ':
                                       break
                          print(c)
            
calc()
