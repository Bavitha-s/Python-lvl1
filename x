# list is a data structure ( is a structure how you store data in it)
# list can be used to store multiple values. (same type or differnt type)
# ages = [10,12,13,14] 
# list can also have mixed data type. 
# student = [1,"Bavitha",12,False,5.5] 
#            0   1        2  3    4   (n-1) where n is length of list 
#           -5  -4       -3 -2   -1
# index will tell you how many element you need to skip to reach that particular element 
student = [1,"Bavitha",12,False,5.5]
# print(student[1])
# print(student[5]) this gives error saying list out of index 
# you cannot go beyond n-1 
# print(student[-6]) list out of index 
# print(len(student))

# list with loop using indexes ( generate all the indexes )
# range(start=0,end,step=1) range of numbers
# print(list(range(5))) # 0,1,2,3,4
# print(range(5)) this is like a closed box 
# for index in range(len(student)):
#     print(student[index])

# list with loops without using indexes 
for detail in student:
    print(detail)




