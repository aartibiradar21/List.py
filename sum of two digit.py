# l=[12,34,57,32]
# i=0
# while i<len(l):
#     a=str(l[i])
#     j=0
#     sum=0
#     while j<len(a):
#         sum=sum+int(a[j])
#         j=j+1
#     i=i+1
#     print(sum)
  









# list1=[1,2,3,4,5]
# list2=[1,2,3,4,5]
# list3=[]
# i=0
# while i<len(list1):
#     b=list1[i]+list2[i]
#     list3.append(b)
#     i=i+1
# print(list3)

list1=[[1,2,3],[4,5,6]]
list2=[[1,2,3],[4,5,6]]
list3=[]
i=0
while i<len(list1):
    j=0
    b=0
    while j<len(list1[i]):
        b=list1[i]+list2[i]
        list3.append(b)
        j=j+1
    i=i+1
print(list3)



