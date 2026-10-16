user_int=input("Enter nummber:")
check=True
for i in range(0,len(user_int)):
    if user_int[i]>'9' or user_int[i]<'0':
        check=False
if check:
    int_type=int(user_int)
    if int_type%2==0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Wrong input type!")
