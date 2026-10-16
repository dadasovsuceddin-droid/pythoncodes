input1=int(input("Enter first number:"))
input2=int(input("Enter second number:"))
input3=int(input("Enter third number:"))
if input1<=input2 and input1<=input3:
    if input2<=input3:
        print(input1,input2,input3)
    else:
        print(input1,input3,input2)
elif input2<=input1 and input2<=input3:
    if input1<=input3:
        print(input2,input1,input3)
    else:
        priint(input2,input3,input1)
else:
    if input1<=input2:
        print(input3,input1,input2)
    else:
        print(input3,input2,input1)