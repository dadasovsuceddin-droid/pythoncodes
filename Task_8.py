#Task 8
pur_amount=float(input("Enter  total amount:"))
if pur_amount<100.00:
    discount=0
elif pur_amount<300.00:
    discount=10
elif pur_amount<500.00:
    discount=15
else:
    discount=20
print("Original Price:",pur_amount,"AZN")
print("Discount:",discount,"%","AZN")
print("Discount amount:",pur_amount/100*discount,"AZN")
print("Final price:",pur_amount-pur_amount/100*discount,"AZN")