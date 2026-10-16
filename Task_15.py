exam_score=int(input("Enter your exam score:"))
school_score=int(input("Enter your school score:"))
age=int(input("Enter your age:"))
if exam_score<0 or exam_score>700 or school_score<0 or school_score>100 or age<=0:
    print("Invalid input")
elif age<16:
    print("Rejected")
elif exam_score>=600 and exam_score<=700:
    print("Congrats!!! You accepted and get scholarship :)")
elif exam_score>=500:
    print("Congrats!!! You accepted")
elif exam_score>=400 and school_score>=80:
    print("Congrats!!! You accepted")
else:
    print("Rejected")