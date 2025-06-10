students=[
    {'name':'Sok','score':85},
    {'name':'Dara',"score":42},
    {'name':'Rith','score':73},
    {'name':'Sophy','score':35},
    {'name':'Mony','score':90}
]
count=0
for i in range(len(students)):
    if students[i]['score']<50:
        count+=1
print(count)