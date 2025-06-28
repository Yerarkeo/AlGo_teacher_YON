# # ex1
# array=[[1,2,3],[4,5,6],[7,8,9]]
# print(array)
# # ex2
# array=[[1,2,3],[4,5,6],[7,8,9]]
# print(array[1][2])
# # ex3
# array=[[1,2,3],[4,5,6],[7,8,9]]
# print(array[2][2])
# # ex4
# array=[[1,2,3],[4,5,6],[7,8,9]]
# print(array[1][2])
# # ex5
# array=[[1,2,3],[4,5,6],[7,8,9]]
# print(array[2][0])
# # ex6
# array=[[1,7,3,4],[5,6,7,8],[9,1,1,1]]
# print(array[0])
# # ex7
# array=[[1,7,3,4],[5,6,7,8],[9,1,1,1]]
# print(array[2])
# # ex8
# array=[[1,7,3,4],[5,6,7,8],[9,1,1,1]]
# result=[]
# for row in array:
#     result.append(row[3])
# print(result)
# # ex9
# array=[[1,7,3],[5,6,7],[9,1,1]]
# for row in range(len(array)):
#    for culomn in range(len(array[row])):
#         if culomn==2-row:
#             print(array[row][culomn])
# ex10
array=[[1,7,3],[5,6,7],[9,1,1]]
result=[]
for row in range(len(array)):
   for culomn in range(len(array[row])):
        if culomn==2-row :
                result.append(array[row][culomn])
result.reverse()
for an in result:
     print(an)