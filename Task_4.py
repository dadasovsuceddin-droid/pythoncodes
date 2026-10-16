#Task 4
studentGrade=int(input("Enter your grade:"))
if studentGrade>100:
    print("Invalid number")
elif studentGrade<0:
    print("Invalid number")
else:
    if studentGrade>=91:
        print("A")
    elif studentGrade>=81:
        print("B")
    elif studentGrade>=71:
        print("C")
    elif studentGrade>=61:
        print("D")
    elif studentGrade>=51:
        print("E")
    else:
        print("F")