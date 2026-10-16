#Task 7
User_age=int(input("Enter your age:"))
if User_age<0 or User_age>200:
    print("Invalid age")
elif User_age<=12:
    print("Child")
elif User_age<=17:
    print("Teenager")
elif User_age<=64:
    print("Adult")
else:
    print("Senior")