day_num=int(input("Enter day number:"))
match day_num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case day_num:
        print("Invalid day number")
        exit()
if day_num>=1 and day_num<=5:
    print("Study day")
else:
    print("Weekend")
