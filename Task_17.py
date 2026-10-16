total=int(input("Enter total(AZN):"))
mem_answer=input('Membership answer(yes or no):')
fee=5
if total<0 or (mem_answer!='yes' and mem_answer!='no'):
    print("Invalid input")
    exit()
if total>=50 or mem_answer=='yes':
    print("Delievery is free. Total is",total,'AZN')
else:
    print("Fee:",fee,"AZN")
    print("Final total",total+fee,"AZN")