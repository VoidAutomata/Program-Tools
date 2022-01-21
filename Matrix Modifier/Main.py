import array
import numpy as np

A1 = np.array([[-1, -2, 3], [4, 0, -4]])
A2 = np.array([[4, -3], [-5, 2], [-1, -2]])
#print(matrix[0,0]);

def multiplyAdd (row1, row2, co):
    #row1 is operator
    #row2 is operated
    #co is "coefficient", or multiplicative operand
    matrix[row2] += matrix[row1]*co

def swap (row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]

def div (row, co):
    matrix[row] = matrix[row] / co

print("to Row Echelon form:")
#swap(2, 0)
#div(0, 2)
#multiplyAdd(0, 2, -2)

A1 = np.transpose(A1)
#print(np.add(A1, A2))
#print(np.dot(A1, A2))
print(np.subtract(np.multiply(A1, 2), A2))
#multiplyAdd(1, 0, -2)



