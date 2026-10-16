side1=int(input("Enter side 1:"))
side2=int(input("Enter side 2:"))
side3=int(input("Enter side 3:"))
if side1<=0 or side2<=0 or side3<=0:
    print("Triangle cannot be created")
elif side1==side2 and side1==side3:
    print("Equilateral")
elif side1+side2>side3 and side1+side3>side2 and side2+side3>side1:
    if side1==side2 or side1==side3 or side2==side3:
        print("Isosceles")
    else:
        print("Scalane")
else:
    print("Triangle cannot be created")