name='yon'
h=len(name)-1
text=''
for i in range(len(name)):
    text+=(name[h-i])
print(text)
nam=''
for i in range(len(name)):
    nam+=name[len(name)-i-1]
print(nam)
texts='abc'
text=''
for i in range(len(texts)):
    text+=texts[len(texts)-i-1]
print(text)


def reverse_string(str):
    result=''
    for i in range(len(str)):
        result+=str[len(str)-i-1]
    return result
print(reverse_string('hi'))
print(reverse_string('yon'))
print(reverse_string('Rady'))
print(reverse_string('yerar'))
def revome_space(str):
    result=''
    for i in range(len(str)):
        if str[i]!=" ":
            result+=str[i]
    return result
print(revome_space('ye rar'))
def hi(name, age,email):
    print(name,age,email)
hi('yerar',21,'yerar@gmail.com')
def sum(n1,n2):
    return n1+n2
x=sum(3,4)+3
def sum1(n1,n2,n3,n4):
    return n1+n2+n3+n4
result= sum1(14,67,34,3)+2
print(result)
print(x)
def introduce(name):
    print('My name is:',name)
introduce('yon')

# ex1:
names=['abc','him','rady','mengheang']
def reverse_string(names):
    result=''
    for i in range(len(names)):
        result+=names[len(names)-i-1]
# work:
array2D = [ [12, 3, 19, 0, 7],
            [8, 14, 6, 32, 17],
            [11, 20, 1, 13, 9],
            [4, 10, 5, 18, 16],
            [0, 15, 3, 19, 6]
            ]
# # ex1:
mac=array2D[0][0]
for rows in array2D:
    for cols in rows:
        if cols>mac:
            mac=cols
print(mac)

# # ex2:

for rows in array2D:
    sum=0
    for cols in rows:
        sum+=cols
    print(sum)
# # ex3:
sum=0
for rows in array2D:
  
    for cols in rows:
        sum+=cols
print(sum)
# # ex4:
target = 19   
count = 0

for row in array2D:
    for item in row:
        if item == target:
            count += 1
print(' specific number appears',target)
