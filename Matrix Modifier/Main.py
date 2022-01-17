import array
import numpy as np

matrix = np.array([[1, -1, -1, 0, -2, 9], [3, 2, -8, 5, 9,-43], [2, -3, -1, -1, -6, 28]])
#print(matrix[0,0]);

def multiplyAdd (row1, row2, co):
    #row1 is operator
    #row2 is operated
    #co is "coefficient", or multiplicative operand
    matrix[row2] += matrix[row1]*co


multiplyAdd(0, 1, -1)
print(matrix)
