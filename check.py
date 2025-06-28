# # ex2:
texts=input('Enter your skill:')
skill=''
for text in texts:
    if text!=" ":
        skill +=text
print(skill)
# # ex3:
texts=input('Enter your name:')
char=input('Enter your char:')
name='' 
counter=0
for u in range(len(texts)):
    if texts[u]==char:
                counter+=1
print('The letter', char,'is',counter)
# # ex4:
arrays=input('enter your array:')
numbers=input('Enter your number:')
counter=0
for i in range(len(arrays)):
    if arrays[i]==numbers:
        counter+=1
print('number', numbers,'is',counter)
# # ex1:

text1 = input("Enter your name:")
counter = 0
for i in range(len(text1)):
    if text1[i] == " ":
        counter = int(i)
counter1 = counter 
result1 = ''
for i in range(len(text1)):
    if i > counter:
        result1 += text1[i]
result2 = ""
result = ''
for i in range(len(text1)):
    if i <= counter:
        result2 += text1[i]
space_line = ''
for i in range(len(text1)):
    if text1[i] == ' ':
        space_line += text1[i]
result += result1 + space_line + result2
print(result)
# # ex1: recheck
text='Hello'
h=len(text)-1
texts=''
for i in range(len(text)):
     texts+=text[h-i]
print(texts)
text='Hello'
result=''
for i in range(len(text)):
    result+=text[len(text)-i-1]
print(result)
arrays=['a','b','c']
result=''
re2=[]
for i in range(len(arrays)):
    result+=arrays[len(arrays)-i-1]
    re2.append(result[i])
print(re2)
# ex2:
arrays=['a','b','c']
re2=[]
for i in range(len(arrays)):
      re2+=arrays[len(arrays)-i-1]
print(re2)

name='yerar'
print(name[0:5])
# ex1
name='class26B'
print(name[2:8])
print(name[2:])
print(name[0:7])
print(name[:7])
print(name[:-1])
print(name[::2])
print(name[:8:2])
print(name[0:8:2])
print(name[0:8:1])
print(name[0:8])
print(name[0:])
print(name[:9:-1])
print(name[::-1])
print(name[5:7])
result=''
for i in range(len(name)):
    if i >=5 and i<=6:
        result+=name[i]
print(result)
# homework
# 1: When we use interger?
# 2:When we use boolean?
# 3: when we use string?
# 4: When we use float?
# 5: When we use =?
# 6: When we use ==?
# 7; When we use arrays or list?
# 8: When we use object or dictionary?
# 9: When we use array object?
# 10: When we use loop?
# 11: When we use while loop?
# 12: When we use for loop?
# 13: When we use loop index?
# 14:When we use loop value?
# 15:when we use function?
# 16: When we need to use parameter of function?
# 17: When function need to return value?
# 18; when we don't need to return value function?
# 19: When we need to use array2D?
# 20: Why need to use "or"?
# 21: Why need to use "and"?
# 22:when we need to plus string?
# 23:When we need to append array?
# 24: when we use > ,< , <= and >=?
# 25: When we use !=?
# 26: When we use loop in loop?
# 27: When we use if elif and else?
# 28: Why we use index?
# 29: when we use key?
# 30: WHen we use pop and append?

# HOMEWORK 02


# Ex01 reverse string in array
#   names = ['abc','him','rady']
#   Expect Result:
#   ['cba','mih','yyar']

# Ex02: count letter "a" of each name
#    ['natiya','yatoya','rady']
#   Expted Result:
#   [2,2,0]

# Ex03: convert name to Upercase
#   ['abc','him','rady']

#   Expected Result:
#   ['ABC','HIM','RADY']

# Ex04: reverse name and convert to uppercase
#  ['abc','him','rady']

#   Expected Result:
#   ['CBA','MIH','YDAR']
# ex1:

names = ['abc','him','rady'] 
def reverse_name(names):
    reverse=[]
    for name in names:
        text=''
        for i in range(len(name)):
            text+=name[len(name)-1-i]
        reverse.append(text)
    print(reverse)
reverse_name(names)
# ex2:
names=['natiya','yatoya','rady']
def count_a(names):
  result=[]
  for name in names:
      counter=0
      for i in range(len(name)):
          if name[i]=='a':
            counter+=1
      result.append(counter)
  print(result)
count_a(names)
# ex3:
names=['abc','him','rady']
def up_name(names):
    result=[]
    for name in names:
        convert=''
        for i in range(len(name)):
                convert +=name[i].upper()
        result.append(convert)
    print(result)
up_name(names)
# ex4:
names=['abc','him','rady']
def reverse_apper(names):
    result=[]
    for name in names:
        reverse=''
        for i in range(len(name)):
            reverse+=name[len(name)-i-1].upper()
        result. append(reverse)
    print(result)
reverse_apper(names)




