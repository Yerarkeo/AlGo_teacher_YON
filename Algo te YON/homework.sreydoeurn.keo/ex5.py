students=[
    {'name':'Sok','score':85},
    {'name':'Dara',"score":42},
    {'name':'Rith','score':73},
    {'name':'Sophy','score':35},
    {'name':'Mony','score':90}
]
sum=0
for i in range(len(students)):
    sum+=students[i]['score']
    average=sum/len(students)
print(average)