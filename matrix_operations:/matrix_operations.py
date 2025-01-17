import numpy as np

# Function for matrix addition
def matrix_addition(matrix1, matrix2):
    return np.add(matrix1, matrix2)

# Function for matrix subtraction
def matrix_subtraction(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

# Function for matrix multiplication
def matrix_multiplication(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# Function for matrix transpose
def matrix_transpose(matrix):
    return np.transpose(matrix)

# Function to calculate matrix determinant
def matrix_determinant(matrix):
    return np.linalg.det(matrix)

# Function for matrix inverse
def matrix_inverse(matrix):
    return np.linalg.inv(matrix)

# Main function to test the operations
if __name__ == "__main__":
    # Sample matrices
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])

    print("Matrix 1:")
    print(matrix1)

    print("Matrix 2:")
    print(matrix2)

    # Perform operations
    print("\nMatrix Addition:")
    print(matrix_addition(matrix1, matrix2))

    print("\nMatrix Subtraction:")
    print(matrix_subtraction(matrix1, matrix2))

    print("\nMatrix Multiplication:")
    print(matrix_multiplication(matrix1, matrix2))

    print("\nMatrix Transpose (Matrix 1):")
    print(matrix_transpose(matrix1))

    print("\nMatrix Determinant (Matrix 1):")
    print(matrix_determinant(matrix1))

    print("\nMatrix Inverse (Matrix 1):")
    print(matrix_inverse(matrix1))
