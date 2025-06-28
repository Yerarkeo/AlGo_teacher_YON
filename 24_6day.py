# # def sum(num1,num2):
# #     return num1+num2
# # sum(2,5)
# def reverse_string(string):
#     result=''
#     for i in range(len(string)):
#         result+=string[len(string)-i-1]
#     return result
# new_arr=[]
# names=['abc','Him','rady']
# for i in range(len(names)):
#     new_arr.append(reverse_string(names[i]))
# print(new_arr)
# # def reverse(string):
# #     result=''
# #     for i in range(len(string)):
# #        result+=string[len(string)-i-1]
# #     return result
# # new_arr=[]
# # names=['yerar','nary','bopha','yeji']
# # for i in range(len(names)):
# #     new_arr.append(reverse(names[i]))  
# # print(new_arr)  
# # def reverse_string(string):
# #     result=''
# #     for i in range(len(string)):
# #         result+=string[len(string)-i-1]
# #     return result
# # new_arr=[]
# # names=['yerar','yuna','yeji', 'ryujin']
# # for i in range(len(names)):
# #     new_arr.append(reverse_string(names[i]))
# # print(new_arr)
# # ex2:
# def revers_string(string):
#     counter=0
#     for i in range(len(string)):
#         if string[i]=='a':
#           counter+=1
#     return counter
# new_arr=[]
# names=['natiya','yatoya','rady']
# for i in range(len(names)):
#     new_arr.append(revers_string(names[i]))
# print(new_arr)
# # ex3:
# def convert_string(string):
#     result=''
#     for i in range(len(string)):
#         if string[i].lower():
#             result+=string[i].upper()
#     return result
# arr=[]
# names=['abc','him','rady']
# for i in range(len(names)):
#     arr.append(convert_string(names[i]))
# print(arr)
# # ex4:
# def reverse_and_convert_string(string):
#     result=''
#     for i in range(len(string)):
#         result+=string[len(string)-i-1].upper()
#     return result
# new_arr=[]
# names=['abc','him','rady']
# for i in range(len(names)):
#     new_arr.append(reverse_and_convert_string(names[i]))
# print(new_arr)
# ex2 repeat
def count_string(string):
    count=0
    for i in range(len(string)):
        if string[i]=='a':
            count+=1
    return count
new_arr=[]
names=['naryta','borina','soriya']
for i in range(len(names)):
    new_arr.append(count_string(names[i]))
print(new_arr)
# ex3repeat
def convert_string(string):
    result=''
    for i in range(len(string)):
        result+=string[len(string)-i-1].upper()
    return result
new_arr=[]
names=['yuna',' Nana','kelly']
for i in range(len(names)):
    new_arr.append(convert_string(names[i]))
print(new_arr)
