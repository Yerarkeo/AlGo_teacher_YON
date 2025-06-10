students=[
    {'name':'Sok','score':85},
    {'name':'Dara',"score":42},
    {'name':'Rith','score':73},
    {'name':'Sophy','score':35},
    {'name':'Mony','score':90}
]
for i in range(len(students)):
    result=len(students)
    for u in range(result-1-i):
        if students[u]['score']<students[u+1]['score']:
            students[u],students[u+1]=students[u],students[u+1]
name=[student['name'] for student in students]
print(','.join(name))