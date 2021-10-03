def display(name,phno,email,phno2=None,email2=None):
             print("Name is :",name)
             print("Phone number is:",phno)
             print("Email is:",email)
             if phno2!=None:
                          print("Alternate number is :",phno2)
             if email2!=None:
                          print("Alternate Email is :",email2)
             print('-'*21)
display('ajay',8889941291,'ajay2028@gmail.com')
display('ajay',8889941291,'ajay2028@gmail.com',123456)
display('ajay',8889941291,'ajay2028@gmail.com',9555445091,'raghvendraajay2028@gmail.com')
display('ajay',8889941291,'ajay2028@gmail.com',phno2=9555445091)
display('ajay',8889941291,'ajay2028@gmail.com',email2='raghvendraajay2028@gmail.com')
