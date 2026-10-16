elec_usage=int(input("Enter electricity usage(kWh):"))
first_rate=0.08
second_rate=0.12
third_rate=0.15
if elec_usage<0:
    print("Invalid input")
elif elec_usage<=100:
    print("Electricity usage:",elec_usage,"kWh")
    print("Applied rate:",first_rate,"AZN/kWh")
    print("Total bill:",first_rate*elec_usage,"AZN")
elif elec_usage<=300:
    print("Electricity usage:",elec_usage,"kWh")
    print("Applied rate:",second_rate,"AZN/kWh")
    print("Total bill:",second_rate*elec_usage,"AZN")
else:
    print("Electricity usage:",elec_usage,"kWh")
    print("Applied rate:",third_rate,"AZN/kWh")
    print("Total bill:",third_rate*elec_usage,"AZN")