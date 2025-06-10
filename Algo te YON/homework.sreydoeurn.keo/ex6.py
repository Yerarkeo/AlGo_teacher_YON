students=[
    {'name':'Sok','score':85},
    {'name':'Dara',"score":42},
    {'name':'Rith','score':73},
    {'name':'Sophy','score':35},
    {'name':'Mony','score':90}
]
student_name=input('Enter student name:')
search=False
for student in students:
    if student['name']==student_name:
        search=True
        print('search:',student)
if not search:
        print('student not found')