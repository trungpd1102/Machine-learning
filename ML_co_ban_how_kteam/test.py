import numpy as np

# # Ma trận 
# _A = [[1,2],[4,5]]
# # Vector
# _B = [[7,1], [1,2]]

# A = np.array(_A, dtype=None)
# B = np.array(_B, dtype=None)

# print('A: \n',A)
# print('B: \n',B)
# # print('A[0,1 ]:',A[0,1])
# # print('A[:,2 ]:',A[:,2])
# print('A[0,0 ]:',A[0,0])
# print(_A[0][0])


# print('A + B: \n', A + B)
# print('A - B: \n', A - B)

# print('A * B: \n', A @ B)
# print('A * B: \n', B @ A)


# C = np.eye(9)

# print(C)


# Phép nhân element-wise

# _a = [ [ 1, 2, 3 ], [ 4, 5, 6 ] ]
# _b = [ [ 2, 3, 5], [7, 9, 21] ]

# a = np.array(_a)
# b = np.array(_b)

# print(a)
# print(b)

# print('a*b: \n', a * b)


# a = np.eye(5)

# print(a == 1)


# Ma trận khả nghịch INVERSE MATRIX (A mũ -1)
# _a = [[ 1, 2, 3 ], [ 4, 5, 6 ]]

# a = np.array(_a)

# a_i = np.linalg.pinv(a)

# print(a)
# print(a_i)
# print(a@a_i)


#Ma trận chuyển vị TRANSPOSE MATRIX (A mũ T)
# _a = [[ 1, 2, 3 ], [ 4, 5, 6 ]]

# a = np.array(_a)

# a_t = np.transpose(a)

# print(a)
# print(a_t)



_a = [[ 1, 2, 3 ], [ 4, 5, 6 ]]

a = np.array(_a)

a_t = np.transpose(a)

print(a)
# print(a_t)
print(np.sum(a,0)) #sum các hàng
print(np.max(a,0)) #max từng hàng
print(np.min(a,0)) #min từng hàng

print(np.sum(a,1)) #sum các cột
print(np.max(a,1)) #max từng cột
print(np.min(a,1)) #min từng cột