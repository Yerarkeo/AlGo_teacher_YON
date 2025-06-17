numbers=[1,2,3,4,5]
num=[]
for i in range(len(numbers)):
    if numbers[i]%2==0:
        num.append(numbers[i])
print(num)
numbers=[1,2,3,4,5]
for i in range(len(numbers)):
    if numbers[i]%2==0:
       print(numbers[i])
numbers=[1,2,3,4,5]
for i in range(len(numbers)):
    if numbers[i]%2==1:
       print(numbers[i])
numbers=[1,2,3,4,5]
num=[]
for i in range(len(numbers)):
    if numbers[i]%2==1:
        num.append(numbers[i])
print(num)
numbers=[1,2,3,4,5]
num=0
for i in range(len(numbers)):
    if numbers[i]%2==0:
        num+=numbers[i]
print(num)
numbers=[1,2,3,4,5]
num=0
for i in range(len(numbers)):
    if numbers[i]%2==1:
        num+=numbers[i]
print(num)
numbers=[1,2,3,4,5]
num=0
for i in range(len(numbers)):
        num+=numbers[i]
print(num)
numbers=[1,2,3,4,5]
num=0
for i in range(len(numbers)):
    if numbers[i]%2==1:
        num+=1
print(num)
numbers=[1,2,3,4,5]
num=0
for i in range(len(numbers)):
    if numbers[i]%2==0:
        num+=1
print(num)

numbers=[1,2,3,4,5]
num=[]
for i in range(len(numbers)):
    if numbers[i]!=2 and  numbers[i]!=4 :
        num.append(numbers[i])
print(num)
numbers=[1,2,3,4,5]
num=[]
for i in range(len(numbers)):
    if numbers[i]%2==0:
        num .append(numbers[i])
print(num)
numbers=[1,2,3,4,5]
for i in numbers[:]:
    if i%2==0:
        numbers.remove(i)
print(numbers)
names=input('Enter your name:')
h=len(names)-1
result=''
for i in range(len(names)):
    result+=names[ len(names)-1-i] +''
print(result)
