# magic=[[8,3,4],
#         [1,5,9],
#         [6,7,2]]
# row_sum=0
# i=0
# while i<len(magic):
#     j=0
#     while j<len(magic):
#         row_sum=row_sum+magic[j][i]
#         j=j+1
#     i=i+1
#     print(row_sum)
#     print()
# i=0
# col_sum=0
# while i<len(magic):
#     j=0
#     while j<len(magic):
#       col_sum=col_sum+magic[j][i]
#       j=j+1
#     i=i+1
#     print(col_sum)
#     print()
# i=0
# left_diagonal=0
# while i<len(magic):
#     j=0
#     while j<len(magic):
#         left_diagonal=left_diagonal+magic[j][i]
#         j=j+1
#     i=i+1
#     print(left_diagonal)
#     print()
# i=0
# right_diagonal=0
# while i<len(magic):
#     j=0
#     while j<len(magic):
#         right_diagonal=right_diagonal+magic[j][i]
#         j=j+1
#     i=i+1
#     print(right_diagonal)
#     print()
# if row_sum==col_sum==left_diagonal==right_diagonal:
#     print("it is a magic square",row_sum,col_sum,left_diagonal,right_diagonal)
# else:
#     print("it is not a magic square",row_sum,col_sum,left_diagonal,right_diagonal)
