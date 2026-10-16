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