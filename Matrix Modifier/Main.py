import array
import numpy as np
from fractions import Fraction

A1 = np.array([[5, 5, 5], [-1, -1, 0], [1, 2, -2]])
A2 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
#print(matrix[0,0]);

def multiplyAdd (matrix, row1, row2, co):
    #row1 is operator
    #row2 is operated
    #co is "coefficient", or multiplicative operand
    matrix[row2] += matrix[row1]*co

def multiplyAdd2 (matrix, matrix2, row1, row2, co):
    #row1 is operator
    #row2 is operated
    #co is "coefficient", or multiplicative operand
    matrix[row2] += matrix[row1] * co
    matrix2[row2] += matrix[row1] * co

def swap (matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]

def swap2 (matrix, matrix2, row1, row2):
    matrix2[[row1, row2]] = matrix2[[row2, row1]]
    matrix[[row1, row2]] = matrix[[row2, row1]]

def div (matrix, row, co):
    matrix[row] = matrix[row] / co

def div (matrix, matrix2, row, co):
    matrix[row] = matrix[row] / co
    matrix2[row] = matrix2[row] / co


#print("to Row Echelon form:")
print(np.linalg.inv(A1))
swap2(A1, A2, 0, 2)
multiplyAdd(A1, 0, 1, 1)
multiplyAdd(A1, 0, 2, -5)
multiplyAdd(A1, 1, 2, 5)
div(A1, 2, 5)
multiplyAdd(A1, 2, 1, 2)
#multiplyAdd2(A1, A2, 0, 1, -3)
#div(A1, 1, 3)



#multiplyAdd(0, 2, -2)

#print(np.add(A1, A2))
#print(np.dot(A1, A2))
print("//")
print(A1)
#print(A2)
#multiplyAdd(1, 0, -2)



