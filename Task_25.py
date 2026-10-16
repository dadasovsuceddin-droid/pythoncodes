stu_ID=input("Enter your stdudent ID:")
age=input("Enter your age:")
workshop_code=input("Enter your workshop code:")
pay_amount=input("Enter payment amount:")
if len(stu_ID)>8:
    print("Wrong student ID format")
for i in stu_ID:
    if i>'9' or i<'0':
        print("Wrong student ID format")
        break
int_age=int(age)
if int_age<16 or int_age>65:
    print("Rejected")
    exit()
amount=0
min_age=0
match workshop_code:
    case 'PY':
        amount=30
        min_age=16
    case 'WEB':
        amount=40
        min_age=16
    case 'CY':
        amount=50
        min_age=18
    case workshop_code:
        print("Rejected")
        exit()
discount=0
if int_age>=16 and int_age<=18:
    discount=20
expense=amount - amount/100*discount
for i in pay_amount:
    if i<'0' or i>'9':
        print("Wrong input style")
        exit()
if float(expense)>float(pay_amount):
    print("Rejected")
    exit()
print("Registration confirmed...")
print("Discount:",amount/100*discount,"AZN")
print("Final fee:",expense,"AZN")
print("Change:",float(pay_amount)-(amount - amount/100*discount),"AZN")

