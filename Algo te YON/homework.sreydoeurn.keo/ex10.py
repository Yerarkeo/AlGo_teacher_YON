students=[
    {'name':'Sok','score':85},
    {'name':'Dara',"score":42},
    {'name':'Rith','score':73},
    {'name':'Sophy','score':35},
    {'name':'Mony','score':90}
]
score=[]
for i in range(len(students)):
    if students[i]['score'] in score:
        score +=students[i]['score']
        print('Duplicates found')
else:
        print('No duplicates')