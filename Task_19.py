dr_code=input("Enter your drink code:")
quantity=int(input("Enter quantity from 1 to 10:"))
drink=''
amount=0
match dr_code:
    case 'T':
        drink='Tea'
        amount=2
    case 'C':
        drink='Coffee'
        amount=4
    case 'J':
        drink='Juice'
        amount=3
    case dr_code:
        print("Wrong drink code")
        exit()
if quantity<1 or quantity>10:
    print("Invalid quantity")
    exit()
print("Drink:",drink)
print("Quantity:",quantity)
print("Price:",amount,"AZN")
if amount>=20: print("Large order")
else: print("Regular order")