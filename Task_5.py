#Task 5
UserNum1=int(input("Enter first number:"))
UserNum2=int(input("Enter second number:"))
UserNum3=int(input("Enter third number:"))
if UserNum1>=UserNum2 and UserNum1>=UserNum3:
    print(UserNum1)
elif UserNum2>=UserNum1 and UserNum2>=UserNum3:
    print(UserNum2)
else:
    print(UserNum3)