balance=1000
pin=input("Enter PIN:")
if pin==' ':
    print("PIN is required")
    exit()
elif len(pin)!=4:
    print("PIN must have 4 digits")
    exit()
else:
    for i in pin:
        if i<'0' or i>'9':
            print("Digits only")
            exit()
correctpin='0427'
if pin==correctpin:
    print("Acces granted")
else:
    print("Incorrect PIN")
amount=input("Enter amount of money:")
for i in pin:
        if i<'0' or i>'9':
            print("Digits only")
            exit()
amount=int(amount)
withdrawl=2
if amount>500 or amount<10 or amount%10!=0:
    print("Not proper to the amount rules")
    exit()
elif amount<=200:
    withdrawl=0
    exit()
if amount + withdrawl <= balance:
    print("Process completed succesfully")
    print("Withdrawl amount:",amount,"AZN")
    print("Fee:",withdrawl,"AZN")
    print("New balance:",balance - amount - withdrawl,"AZN")
    
    
    
    
    
    
    

