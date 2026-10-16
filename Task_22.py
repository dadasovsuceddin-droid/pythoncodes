phone_number=input("Enter active phone number:")
for i in phone_number:
    if i<'0' or i>'9':
        print("Digits only")
        exit()
if len(phone_number)!=10:
    print("Number contains 10 digits")
elif phone_number[0]!='0':
    print("Begin with 0")
prefix=phone_number[0]+phone_number[1]+phone_number[2]
match prefix:
    case '050' | '051' | '055' | '070' | '077' | '099':
        print("Accepted")
    case prefix:
        print("Wrong prefix")