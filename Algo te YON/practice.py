students=[
    {'name':'Sok','score':85},
    {'name':'Dara',"score":42},
    {'name':'Rith','score':73},
    {'name':'Sophy','score':35},
    {'name':'Mony','score':90}
]
# q1
for i in range(len(students)):
    print("Name:",students[i]['name'],',Score:',students[i]['score'])
# q2
for i in range(len(students)):
    if students[i]['score']>=50:
        print(students[i]['name'])
# q3
count=0
for i in range(len(students)):
    if students[i]['score']<50:
        count+=1
print(count)
# q4
for i in range(len(students)):
    mix=students[i]['score']
    if students[i]['score']>mix:
        mix=students[i]['score']
print(students[i]['name'],'with score',mix)

# q5
sum=0
for i in range(len(students)):
    sum+=students[i]['score']
    average=sum/len(students)
print(average)
# q6
student_name=input('Enter student name:')
search=False
for student in students:
    if student['name']==student_name:
        search=True
        print('search:',student)
if not search:
        print('student not found')
# # q8

for i in range(len(students)):
        students[i]['score']=students[i]['score']+5
        print(students[i]['name'],students[i]['score'])
# q10
score=[]
for i in range(len(students)):
    if students[i]['score'] in score:
        score +=students[i]['score']
        print('Duplicates found')
else:
        print('No duplicates')
# q9
result=''
for i in range(len(students)):
    if students[i]['score']>40:
        result+=students[i]['name'] +','
print(result[:-1])


# Correction:
students=[
    {'name':'Sok','score':85},
    {'name':'Dara',"score":42},
    {'name':'Rith','score':73},
    {'name':'Sophy','score':35},
    {'name':'Mony','score':90}
]
# # ex1:
for i in range(len(students)):
    print('Name:',students[i]['name']+", Score: ",students[i]['score'])
# # # f
for i in range(len(students)):
    print(f'Name:{students[i]['name']},Score:{students[i]['score']}')
# ex2:
for student in students:
    if student['score']>=50:
        print(student['name'])
# ex3:
count=0
for student in students:
    if student['score']<50:
        count+=1
print(count)
# ex4:
score=students[0]['score']
for i in range(len(students)):
    if students[i]['score']>score:
        score=students[i]['score']
print(score)

