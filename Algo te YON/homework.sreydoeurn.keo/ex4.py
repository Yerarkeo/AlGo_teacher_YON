students=[
    {'name':'Sok','score':85},
    {'name':'Dara',"score":42},
    {'name':'Rith','score':73},
    {'name':'Sophy','score':35},
    {'name':'Mony','score':90}
]
# ex1
for i in range(len(students)):
    mix=students[i]['score']
    if students[i]['score']>mix:
        mix=students[i]['score']
print(students[i]['name'],'with score',mix)
# ex2
score=students[0]['score']
for i in range(len(students)):
    if students[i]['score']>score:
        score=students[i]['score']
print(score)