import array
import numpy as np

matrix = np.array([[1, 2, -2, 7], [-1, 0, 4, -13], [1, -1, -4, 12]])
#print(matrix[0,0]);

def multiplyAdd (row1, row2, co):
    #row1 is operator
    #row2 is operated
    #co is "coefficient", or multiplicative operand
    matrix[row2] += matrix[row1]*co

def swapRow (row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]

def div (row, co):
    matrix[row] = matrix[row] / co

print("to Row Echelon form:")
#multiplyAdd(0, 1, -1)
multiplyAdd(0, 1, 1)
multiplyAdd(0, 2, -1)
div(1, 2)
multiplyAdd(1, 2, 3)
print(matrix)
print("to Reduced Row Echelon form:")
multiplyAdd(1, 0, -2)
multiplyAdd(2, 1, -1)
multiplyAdd(2, 0, 4)
print(matrix)