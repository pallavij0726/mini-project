import numpy as np

# Create 2D array
matrix = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("Original Matrix:\n", matrix)

# Matrix Transpose
transpose = matrix.T
print("\nTranspose:\n", transpose)

# Matrix Addition
addition = matrix + 10
print("\nAddition (matrix + 10):\n", addition)

# Matrix Multiplication
multiplied = np.dot(matrix, transpose)
print("\nMatrix Multiplication:\n", multiplied)

# Statistical operations
print("\nMean:", np.mean(matrix))
print("Median:", np.median(matrix))
print("Standard Deviation:", np.std(matrix))
