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
# # q2
for i in range(len(students)):
    if students[i]['score']>=50:
        print(students[i]['name'])
# # q3
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

# # q5
sum=0
for i in range(len(students)):
    sum+=students[i]['score']
    average=sum/len(students)
print(average)
# # q6
student_name=input('Enter student name:')
search=False
for student in students:
    if student['name']==student_name:
        search=True
        print('search:',student)
if not search:
        print('student not found')
# # # q8

for i in range(len(students)):
        students[i]['score']=students[i]['score']+5
        print(students[i]['name'],students[i]['score'])
# # q10
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
# # # ex1:
for i in range(len(students)):
    print('Name:',students[i]['name']+", Score: ",students[i]['score'])
# # # # f
for i in range(len(students)):
    print(f'Name:{students[i]['name']},Score:{students[i]['score']}')
# # ex2:
for student in students:
    if student['score']>=50:
        print(student['name'])
# # ex3:
count=0
for student in students:
    if student['score']<50:
        count+=1
print(count)
# # ex4:
score=students[0]['score']
for i in range(len(students)):
    if students[i]['score']>score:
        score=students[i]['score']
print(score)
# ex5:
sum=0
for i in range(len(students)):
    sum+=students[i]['score']
print(sum/len(students))
#     # q1
sum=0
for student in students:
    sum+=student['score']
avg=sum/len(students)
print(avg)
# # ex6:
stu=input('enter studetn name:')
for student in students:
    if stu==student['name']:
        print(f"{student['name']}'s score is {student['score']}")
#         # q1
stu=input('enter studetn name:')
for student in students:
    if stu==student['name']:
        print(student['name']+"'s score is "+str(student['score']))

# ex9:
for student in students:
    if student['score']>40:
        print(student['name'])
# ex8:
stu=[]
for student in students:
    if student['score']>=60:
        stu.append(student['name'])
print(stu)

# q1
arrays=[1,2,3,4,5]
array=[]
for i in range(len(arrays)):
    if arrays[i]%2==0:
        array.append(arrays[i])
print(array)
arrays=[1,2,3,4,5]
array=[]
for i in range(len(arrays)):
    if arrays[i]%2==1:
        array.append(arrays[i])
print(array)
array=[]
for arr in arrays:
    if arr%2==0:
        array.append(arr)
print(array)
array=[]
for arr in arrays:
    if arr%2==1:
        array.append(arr)
print(array)

# # 1:
fruits=[
    {'name':'Apple','qty':2, 'price':20},
    {'name':'Banana','qty':0, 'price':30},
    {'name':'Pine Apple','qty':0, 'price':40},
    {'name':'Wood Apple','qty':2, 'price':10},  
    ]
# # # ex1:
outOfStock=[]
for i in range(len(fruits)):
    if fruits[i]['qty']==0:
        outOfStock.append(fruits[i]['name'])
print(outOfStock)
# # # ex2
smallerthen20=[]
for i in range(len(fruits)):
    if fruits[i]['price']<=20:
       smallerthen20.append(fruits[i]['name'])
print(smallerthen20)
# # ex3:
addMoreQty=[]
for i in range(len(fruits)):
    if fruits[i]['qty']==0:
        fruits[i]['qty']+=5
    addMoreQty.append(fruits[i])
print(addMoreQty)
#     # 1st
new_array=[]
for fruit in fruits:
    if fruit['qty']==0:
       fruits['qty']=5
       new_array.append(fruit)
    else:
        new_array.append(fruit)
print(new_array)
# 2nd
for i in range(len(fruits)):
    if fruits[i]['qty']==0:
        fruits[i]['qty']==5
print(fruits)
# 3th
for fruti in fruits:
    if fruits[i]['qty']==0:
        fruits[i]['qty']=5
print(fruits)
# ex1:
numbers=[1,2,3,9,2,9,9,4]
num=[]
for i in range(len(numbers)):
    if numbers[i]!=9:
      num.append(numbers[i])
print(num)
# ex2:
numbers=[1,2,3,9,2,9,9,4]
for i in range(len(numbers)):
    if numbers[i]==9:
        numbers[i]=5
print(numbers)
# ex3:
numbers=[1,2,3,9,2,9,9,4]
for i in range(len(numbers)):
   if numbers==9:
      numbers[3]=5
print(numbers)
# ex4:
numbers=[1,2,3,9,2,9,9,4]
sumOdd=0
sumEven=0
for i in range(len(numbers)):
    if numbers[i]%2==1:
        sumOdd+=numbers[i]
    if numbers[i]%2==0:
        sumEven+=numbers[i]
print('"Odd":',sumOdd,",",'"Even:"',sumEven)
# ex5
numbers=[1,2,3,9,2,9,9,4]
countOdd=0
countEven=0
for i in range(len(numbers)):
    if numbers[i]%2==1:
        countOdd+=1
    if numbers[i]%2==0:
        countEven+=1
print('"Odd":',countOdd,",",'"Even:"',countEven)

    
