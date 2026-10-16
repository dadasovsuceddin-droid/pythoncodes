user_age=int(input("Please enter your age:"))
user_salary=int(input("Enter your salary(AZN):"))
user_loan=int(input("Enter your requested loan:"))
if user_loan<=0 or user_salary<=0 or user_age<=0:
    print("Invalid input")
elif user_age<18:
    print("Not approved")
elif user_salary<500:
    print("Not approved")
elif user_loan>10*user_salary:
    print("Not approved")
else:
    print("Approved... Congrats!!!")