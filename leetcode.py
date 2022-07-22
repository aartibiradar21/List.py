# l=[1,0,5,0,7,0,5,6,0,3]
# for i in l:
#     if i==0:
#         l.append(i)
#         l.remove(0)
#         # l.append(i)
# print(l)






# l1=[2,3,7]
# l2=[4,5,8]
# l=[]
# s=""
# d=""
# i=1
# while i<len(l1)+1:
#     s+=str(l1[-i])
#     d+=str(l2[-i])
#     i+=1
# b=(int(s)+int(d))
# print(b)
# c=str(b)
# e=""
# for i in range (1,(len(c)+1)):
#     e+=c[-i]
# print(e)



# l=[1,2,3,4,2,4,6,2,5,1,6,8,9,4]
# l=(set(l))
# print(list(l))


# l=[[1,2,3],[4,5,6],[7,8,9]]
# a=[]
# l1=[]
# l2=[]
# l3=[]
# i=1
# while i<=len(l):
#     j=0
#     while j<len(l[-i]):
#         if j==0:
#             l1.append(l[-i][j])
#         elif j==1:
#             l2.append(l[-i][j])
#         elif j==2:
#             l3.append(l[-i][j])
#         j=j+1
#     i=i+1
# a.append(l1)
# a.append(l2)
# a.append(l3)
# print(a)


# l=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# a=[]
# l1=[]
# l2=[]
# l3=[]
# l4=[]
# i=1
# while i<=len(l):
#     j=0
#     while j<len(l[-i]):
#         if j==0:
#             l1.append(l[-i][j])
#         elif j==1:
#             l2.append(l[-i][j])
#         elif j==2:
#             l3.append(l[-i][j])
#         elif j==3:
#             l4.append(l[-i][j])
#         j=j+1
#     i=i+1
# a.append(l1)
# a.append(l2)
# a.append(l3)
# a.append(l4)
# print(a)



# l1 = [1,2,4]
# l2 = [1,3,4]
# i=0
# l3=[]
# while i<len(l1):
#     l3.append(l1[i])
#     l3.append(l2[i])
#     i+=1
# print(l3)


# a= [4,5,1,9]
# i=0
# while i<len(a):
#     if i==1:
#         a.pop(i)
#     i+=1
# print(a)
    
# b= [4,5,1,9]
# i=0
# while i<len(b):
#     if i==2:
#         b.pop(i)
#     i=i+1
# print(b) 


# num=[1,2,2]
# i=0
# while i<len(num):
#     if i==1:
#         print(i)
#     i=i+1

# l=[1,2,3,4,5,6,7]
# i=0
# a=[]
# a1=[]
# while i<len(l):
#     if l[i]>4:
#         a.append(l[i])
#     else:
#         a1.append(l[i])
#     i=i+1
# a.extend(a1)
# print(a)



# s = ["h","e","l","l","o"]
# l=[]
# i=0
# while i<len(s):
#     i=i+1
#     l.append(s[-i])
# print(l)


# a= [1,2,3,4,5]
# l=[]
# i=0
# while i<len(a):
#     i=i+1
#     l.append(a[-i])
# print(l)



# x=123
# i=0
# while i<x:
#     a=x%10
#     x//=10
#     print(a,end="")
# print()
# i=i+1


# a = "AmanaplanacanalPanama"
# i=0
# n=[]
# while i<len(a):
#     str=a[i]
#     c=""
#     j=1
#     while j<len(a[i])+1:
#         c=c+a[i][-j]
#         j=j+1
#     if str==c:
#         n.append(str)
#     i=i+1
# print(n,"is palindrome")


# a="-45"
# b=int(a)
# print(b)


# c="876"
# d=int(c)
# print(d)

# l=[1,2,3,4,5]
# i=0
# while i<len(l):
#     if i==3:
#         l.pop(i)
#     i=i+1
# print(l)


# num=int(input("enter the no"))
# i=0
# while i<=num:
#     if i%3==0 and  i%5==0:
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     i=i+1
# print(i)

# n=int(input("enter the no"))
# l=[]
# i=0
# while i<n:
#     name=input("enter the name")
#     l.append(name)
#     i=i+1
# print(l)


# a=int(input("enter"))
# b=int(input("enter"))
# sum=0
# i=1
# while i<=b:
#     sum+=a
#     i+=1
# print(sum)

# a=["Agale","pratiksha","pratu"]
# i=0
# max=0
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#         l=a[i]
#     i+=1
# print(l)

# a=[2,1,3,4,5]
# i=0
# min=a[i]
# while i<len(a):
#     if (a[i])<min:
#         min=a[i]
#     i+=1
# print(min)
        
# a=[[2,3],5,4,[[7,8],9],10]
# print(a[4])
