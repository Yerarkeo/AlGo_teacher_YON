students=[
    {'name':'Sok','score':85},
    {'name':'Dara',"score":42},
    {'name':'Rith','score':73},
    {'name':'Sophy','score':35},
    {'name':'Mony','score':90}
]
for i in range(len(students)):
        students[i]['score']=students[i]['score']+5
        print(students[i]['name'],students[i]['score'])