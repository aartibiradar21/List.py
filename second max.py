# numbers=[50,40,23,70,56,12,5,10,7]
# max=0
# min=0
# for i in range(len(numbers)):
#     if numbers[i]>max:
#         min=max
#         max=numbers[i]
#     elif numbers[i]>min and min!=numbers[i]:
#          min=numbers[i]
#     else:
#         print("second max",min)




# numbers=[50,40,23,70,56,98,12,5,10,7]
# i=0
# a=0
# while i<len(numbers):
#     if numbers[i]>a:
#         a=numbers[i]
#     i=i+1
# i=0
# b=0
# while i<len(numbers):
#     if numbers[i]>b:
#         if numbers[i]!=a:
#             b=numbers[i]
#     i=i+1
# print(b)

n=[50,40,23,70,56,12,5,10,7] 
i=0
while i<len(n):
    a=n[i]
    if a>n[0] and a<n[3]:
        print("second max",a)
    i=i+1



