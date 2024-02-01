import numpy as np
import numpy.linalg as la

# a)
A1 = np.array([[5, 3], [2, 1]])
B1 = np.array([[9], [4]])
# b)
A2 = np.array([[2, 1, 1], [1, 3, 1], [2, 1, 2]])
B2 = np.array([[6], [2], [9]])
# c)
A3 = np.array([[1, 1, 3], [3, 1, 1], [2, 1, 2]])
B3 = np.array([[-1], [5], [2]])

result1 = la.inv(A1).dot(B1)
X1, Y1 = result1[0], result1[1]

result2 = la.inv(A2).dot(B2)
X2, Y2, Z2 = result2[0], result2[1], result2[2]

# c) kohdan tulos antaa error koska käänteismatriisi ei ole mahdollinen kyseisille matriiseille, koska saavutaan tulokseen jolloin 0 = 0.
# result3 = la.inv(A3).dot(B3)
# X3, Y3, Z3 = result3[0], result3[1], result3[2]

print(f'a) X = {X1}, Y = {Y1}')
print(f'b) X = {X2}, Y = {Y2}, Z = {Z2}')
# print(f'c) X = {X3}, Y = {Y3}, Z = {Z3}')
