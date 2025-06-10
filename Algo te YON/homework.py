# work1
students=[
    {'name': 'Alice','age':17,'score':85,'subject':"Math"},
    {'name': 'Bob','age':16,'score':78,'subject':"English"},
    {'name': 'Charlie','age':18,'score':92,'subject':"Science"},
    {'name': 'Dara','age':17,'score':60,'subject':"History"},
    {'name': 'sokha','age':16,'score':88,'subject':"computer"},
]
for i in range(len(students)):
    print(students[i]['name'],'is',students[i]['age'],'years old,','scored',students[i]['score'],'in',students[i]['subject'],'.')

#work2
students=[
    {'name':"Alice",
     'age':17,
     'gender':'female',
     'Address':{
        'city':"phnom Penh",
        'disstrict': 'Chamkarmon'
        },
     'subjects':[
            {'name': 'math','score':85},
            {'name':'Physics','score':78},
            {'name':'Biology','score':90}]},
    {'name': "sokha",
     "age": 16,
     'gender':'male',
     "Address":
             {'city':'siem Reap',
              'district': 'Svay Dangkum'},
     'subjects': [
                  {'name':'English','score':75},
                  {'name':'Computer','score':88},
                  {'name':'art','score':92}
              ]},
    {'name':'Dara',
     'age':18,
     'gender':'male',
     'address':
                {'city':'battambang',
                'district':'Battambang'},
     'subjects':[
                {'name':'History','score':60},
                {'name':'Geography','score': 70},
                {'name':'math','score':80}
                  ]
              }
]
# q1
counter=0
for student in students:
    if student['gender']== 'male':
        counter+=1
print(counter)
# q2
counter=0
for student in students:
    for subject in student['subjects']:
        if subject['name']=='math':
         counter+=1
print(counter)
# q2
for student in students:
    if student['name']=='sokha':
        scores= [subject['score']
        for subject in student['subjects']]
        count= sum(scores)/len(scores)
print(count)
# q3
for student in students:
    if student['name']=='sokha':
        scores=[]
        for sub in student['subjects']:
            scores.append(sub['score'])
# q4
print(sum(scores)/len(scores))
for student in students:
    if student['name']=='Dara':
        sum=0
        for total in student['subjects']:
            sum+=total['score']
        print(sum)