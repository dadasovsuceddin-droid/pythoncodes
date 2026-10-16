account_balance=1000
withdrawl_amount=int(input("Please enter withdrawl amount(without currency):"))
if withdrawl_amount<=0:
    print("Invalid amount")
elif withdrawl_amount>account_balance:
    print( "Insufficient balance")
else:
    print("Remaining balance :",account_balance - withdrawl_amount,"AZN")