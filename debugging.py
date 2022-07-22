# name=["savitri","phule","26"]
# print(name[0]+name[1])



# num=input("enter the number")
# i=0
# a=""
# k=[]
# while i<len(num):
#     a+=num[i]
#     j=1
#     while j<=len(num)-(i+1):
#         a+="0"
#         j=j+1
#     if i==(len(num)-1):
#         pass
#     else:
#         a+="+"
#     i=i+1
# k.append(a)
# print(k)


    

# l=[['a','b'],['c','d']]

# for i in (l[0]):
#     for j in (l[1]):
#         a=i+j
#         print(a)


# l=[[1,2],[],[],[],[3,4]]
# a=[]
# for i in range(len(l)):

#     if len(l[i])>=1:

#         a.append(l[i])

# print(a)

# l=[1,2,3,4,[5,6,7,8],[9,10,11],12]
# i=0
# sum=0
# while i<len(l):
#     if type(l[i])==list:
#         j=0
#         while j<len(l[i]):
#             sum=sum+l[i][j]
#             j=j+1
#     else:
#         sum=sum+l[i]
#     i=i+1
# print(sum)
    
# l=[[1,2,3],[1,2,3,4],[1,2,3,4,5,6],[5,6,7,8]]
# i=0
# largest=len(l[i])
# while i<len(l):
#     if len(l[i])>largest:
#         largest=len(l[i])
#         a=l[i]
#     i=i+1
# print('largest len is-',largest)
# print('list is-',a)

 
# l=[[1,2,3],[1,2,3,4],[1,2,3,4,5,6],[5,6,7,8]]
# i=0
# largest=len(l[i])
# while i<len(l):
#     if len(l[i])>largest:
#         largest=len(l[i])
#     i=i+1
# print("largest len of list",largest)

# num=int(input("Enter any number between 1 to 7 : "))
# if num==1:
#     print("Sunday")
# elif num==2:
#     print("Monday")
# elif num==3:
#     print("Tuesday")
# elif num==4:
#    print("Wednesday")
# elif num==5:
#    print("Thursday")
# elif num==6:
#    print("Friday")
# elif num==7:
#    print("Saturday")
# else:
#    print("Please enter number between 1 to 7")