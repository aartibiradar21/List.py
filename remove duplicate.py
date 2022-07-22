# a=[1,2,3,4,5,6,7,8,98]
# b=[1,3,2,4,6,9,7]
# i=0
# k=[]
# while i<len(a):
#     if a[i] not in b:
#         k.append(a[i])
#     i=i+1
# print(k)




# l=[1,2,3,4,5,6,4,5,7,9,2,3,8,9]
# l=(set(l))
# print(list(l))




 
# a = [1,2,3,1,2,2]
# i=0
# b=[]
# while i<len(a):
#     if a[i]not in b:
#         b.append(a[i])
#     i=i+1
# print(b)





# a=[1,2,3,2,1]
# i=0
# while i<len(a):
#     j=i
#     while j<len(a):
#         if a[i]==a[j]:
#             a.remove(a[j])
#         j=j+1
#     i=i+1
# print(a)



# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# i=0
# k=[]
# while i<len(n):
#     if n[i] not in k:
#         k.append(n[i])
#     i=i+1
# print(k)

# num=int(input("enter "))
# r=0
# def recur_reverse(num):
#     global r
#     if num>0:
#         reminder=num%10
#         r=(r*10)+reminder
#         recur_reverse(num//10)
#     return r
# r=recur_reverse(num)
# print(r)

# l=[1,2,3]
# l1=[]
# i=0
# while i<len(l):
#     if l[i]!=(l[0]) and l[i]!=(l[2]):
#         l1.append(l[i])
#     i=i+1
# print(l1)


