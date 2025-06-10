# #list Dictionary( Array object)
# student=[
#     {'name':'sreydoeurn','class':'2026B'},
#     {'name':'sokkeang','class':'2026B'},
#     {'name':'darika','class':'2026C'},
#     {'name':'king','class':'2026C'},
#     {'name':'visa','class':'2026A'},
#     {'name':'Seavmey','class':'2026A'}
#         ]
# print(student[5])
# print(student[2]['name'])
# for i in range(len(student)):
#     print((student[i]['name'] ))
# for i in range(len(student)):
#     print((student[i]['class']))
# for i in range(len(student)):
#     print(student[i]['name'],student[i]['class'])
#q1
fruits=[
    {'name':'apple','qty':4,'prize':2,"in_stock":True},
    {'name':'banana','qty':3,'prize':4,"in_stock":False},
    {'name':'banana','qty':6,'prize':2,"in_stock":True},
    {'name':'dragon_fruit','qty':9,'prize':4,"in_stock":False},
    {'name':'kiwi','qty':4,'prize':5,"in_stock":True}
    ]
# # q2
for i in range(len(fruits)):
    print(fruits[i])
# q3
sum=0
for i in range(len(fruits)):
    sum+=fruits[i]['prize']
print(sum)
# q4
sum=0
for i in range(len(fruits)):
    sum+=fruits[i]['qty']
print(sum)
# q5
counter=0
for i in range(len(fruits)):
    if fruits[i]['in_stock']==False:
        counter+=1
print(counter)
sum=0
for i in range(len(fruits)):
    sum+=fruits[i]['qty']
print(sum/len(fruits))
counter=0
for i in range(len(fruits)):
    if fruits[i]['prize']>=2:
        counter+=1
print(counter)
           