# ex1:
def get_first_index(numbers):
    first_index=False
    index=None
    for i in range(len(numbers)):
        if numbers[i]==7 and first_index==False:
            index=i
    return index
print(get_first_index([2,3,7,3,7,7,2]))
# ex2:
def get_first_index(numbers):
    first_index=False
    index=None
    for i in range(len(numbers)):
        if numbers[i]==7 and first_index==False:
            index=i
            first_index=True
    return index
print(get_first_index([2,3,7,3,7,7,2]))
# ex3:
def get_first_index(numbers):
    first_index=False
    index=None
    for i in range(len(numbers)):
        if numbers[i]==7 and first_index==False:
            index=i
            first_index=True
    return index
numbers=[
    [1,4,5,2,4,7,7,2,7],
    [1,4,7,2,4,7,7,2,7],
    [1,7,5,2,4,7,7,2,7],
    [7,4,5,2,4,7,7,2,7]
]
for i in range(len(numbers)):
    print(get_first_index(numbers[i]))
# ex4:
def get_first_index(numbers):
    first_index=False
    index=None
    for i in range(len(numbers)):
        if numbers[i]==7 and first_index==False:
            index=i
            first_index=True
    return index
new_arr=[]
numbers=[
    [1,4,5,2,4,7,7,2,7],
    [1,4,7,2,4,7,7,2,7],
    [1,7,5,2,4,7,7,2,7],
    [7,4,5,2,4,7,7,2,7]
    ]
for i in range(len(numbers)):
    new_arr.append(get_first_index(numbers[i]))
print(new_arr)
# ex5:
def get_first_index(numbers):
    first_index=False
    index=None
    for i in range(len(numbers)):
        if numbers[i]==7 and first_index==False:
            index=i
            first_index=True
    return index
numbers=[
    [1,4,5,2,4,7,7,2,7],
    [1,4,7,2,4,7,7,2,7],[
        1,7,5,2,4,7,7,2,7
    ],
    [7,4,5,2,4,7,7,2,7]
]
new_arr=[]
for i in range(len(numbers)):
    if get_first_index(numbers[i])%2==0:
        new_arr.append(get_first_index(numbers[i]))
print(new_arr)
# ex6:
def please_input(arr,num):
    index=None
    get_first_index=False
    for i in range(len(arr)):
        if arr[i]==num and get_first_index!=True:
            index=i
            get_first_index=True
    return index
arr= eval(input('Enter arr:'))
num=int(input('Enter num:'))
print(please_input)