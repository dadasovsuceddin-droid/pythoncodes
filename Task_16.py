exam_score=int(input("Enter your exam score:"))
min_score=51
Answer=''
if exam_score<0 or exam_score>100:
    print("Invalid input")
elif exam_score>=min_score:
    Answer+='Pass'
else:
    Answer+='Fail'
print(Answer)