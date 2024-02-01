import numpy as np
# luodaan matriisit A ja B
A = np.array([[-1, 2], [3, -5]])
B = np.array([[2, 0], [-1, 4]])
# laskutoimitus 2A+3B
result1 = (2*A + 3*B)
# laskutoimitus A-B
result2 = (A - B)

print(result1)
print()
print(result2)
