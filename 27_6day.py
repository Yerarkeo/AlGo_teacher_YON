# # # ex1:
# user_input=int(input('please enter 7:'))
# while user_input !=7:
#     user_input=int(input('Try again!'))
# # # ex2:
# is_seven=False
# while not is_seven:
#     user_input=int(input('Please enter 8:'))
#     if user_input==8:
#         is_seven=True
#         print('Correct!')
# # #ex3:
# email=input('Input your email:')
# password=input('input your password:')
# while email!='admin@gmail.com' and password!='1234567':
#     print('Your email invalid')
#     email=input('Input your email:')
#     password=input('input your password:')
# # # ex4:
# email=input('Input email :')
# pws=input('Input pas:')
# count=1
# while email!='admin@gmail.com' and pws!='1234567' and count<3:
#     count+=1
#     print('your gmail are invalid')
#     email=input('Input email :')
#     pws=input('Input pas:')
# if count>=3:
#     print('You try more three time will lock!')
# # # # ex5:
# def validate(email,pws):
#     correct=False
#     if email=='admin@gamil.com' and pws=='12345667':
#         correct=True
#     return correct
# email=input('Input Your Gmail:')
# pws=input('Input your pws:')
# count=1
# while email!='admin@gmail.com' and pws != '1234567' and count<3:
#     count+=1
#     print('your gmail is invalid')
#     email=input('Input Your Gmail:')
#     pws=input('Input your pws:')
# if count>=3:
#     print('you try more than tree times will lock!')
# # # ex6:
# def remove_minus(string):
#     result=''
#     for char in string:
#         if char !='-':
#             result+=char
#     return result
# is_contin=True
# while is_contin:
#     word=input('enter your word with minus:')
#     print(f'Yoru word without minus is {remove_minus(word)}')
#     check = input("Do you want to continue('Y/N'):")
#     if check.upper()!='Y':
#         is_contin=False
# ex7:
# def sum(num1,num2):
#     return num1+num2
# num1= int(input('num1:'))
# num2= int(input('num2:'))
# print(sum(num1,num2))

# # ex8:
# def sum(num1,num2):
#     return num1+num2
# total=0
# count=int(input('Enter your number of value :'))
# for i in range(count):
#     num=int(input(f'value {i}:'))
#     total = sum(total,num)
# print(total)

# ex9:
def sum(num1,num2):
    return num1+num2
start=int(input('Enter start value:'))
end= int(input("Enter end value:"))
total=0
for i in range(start,end+1):
    total=sum(total,i)
print(f'sum of number between {start} and {end} is :{total}')