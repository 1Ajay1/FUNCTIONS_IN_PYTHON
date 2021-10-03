user_data={'123456789':{'PIN':'1234','BAL':1000},'987654321':{'PIN':'1234','BAL':10000}}
def validate_data(customer_number):
             if customer_number in user_data: 
                          return True
             return False
def check_pin(cardnum,pin):
             if cardnum in user_data and pin==user_data[cardnum]['PIN']:
                          return True
             return False
def validate_bal(customer_number,bal):
             if bal>user_data[customer_number]['BAL']:
                          return False
             return True

def frontpage(cardnum):
             n=int(input(print("for withdrow press 1,for show account balace press 2")))
             if n==2:
                          print(user_data[cardnum]['BAL'])
             elif n==1:
                          amount=int(input("Enter the amount"))
                          checkamount=validate_bal(cardnum,amount)
                          if checkamount:
                                       user_data[cardnum]['BAL']-=amount
                                       print("Your amount debited",amount, "succesfully")
                                       print("Your remaining amount is ",user_data[cardnum]['BAL'])
                          else:
                                       print("Your amount less than yo entered amount")
def display():
             print("Welcome please insert your card")
             cardnum=input("Enter the card number")
             check=validate_data(cardnum)
             if check:
                          pin=input("Enter the PIN")
                          pincheck=check_pin(cardnum,pin)
                          if pincheck:
                                       frontpage(cardnum)
                          else:
                                       print("Enter the currect PIN")
             else:
                          print("This User not Present in my database")
display()
                          
             
