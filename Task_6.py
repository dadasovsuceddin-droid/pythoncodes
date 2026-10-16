#Task 6
FirstNum=int(input("Enter first number:"))
SecondNum=int(input("Enter second number:"))
operation=input("Enter operation:")
if operation=='+':
    print(FirstNum+SecondNum)
elif operation=='-':
    print(FirstNum- SecondNum)
elif operation=='*':
    print(FirstNum* SecondNum)
elif operation=='/':
    if SecondNum==0:
        print("Error")
    else:
        print(FirstNum/SecondNum)
elif operation=='%':
    if SecondNum==0:
        print("Error")
    else:
        print(FirstNum%SecondNum)
elif operation=='**':
    print(FirstNum**SecondNum)
elif operation=='//':
    print(FirstNum//SecondNum)
else:
    print("Invalid operation")