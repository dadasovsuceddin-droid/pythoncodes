distance=int(input("Enter distance(km):"))
inital_fee=2
first_rate=0.7
second_rate=0.6
third_rate=0.5
if distance<0:
    print("Invalid distance")
elif distance<=5:
    print("Starting fee:",inital_fee,"AZN")
    print("Distance fee:",first_rate,"AZN/km")
    print("Total fee:",inital_fee+first_rate*distance,"AZN")
elif distance<=15:
    print("Starting fee:",inital_fee,"AZN")
    print("Distance fee:",second_rate,"AZN/km")
    print("Total fee:",inital_fee+second_rate*distance,"AZN")
else:
    print("Starting fee:",inital_fee,"AZN")
    print("Distance fee:",third_rate,"AZN/km")
    print("Total fee:",inital_fee+third_rate*distance,"AZN")