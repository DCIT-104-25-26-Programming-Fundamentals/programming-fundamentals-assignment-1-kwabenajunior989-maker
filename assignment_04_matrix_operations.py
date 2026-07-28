# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# ============================================================================
#YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols, label=""):
    print(f"Enter {label} matrix:")
    matrix = []
    for i in range(rows):
        row_input = input(f"Enter row {i + 1}: ")
        row = row_input.split()         
        row = [int(num) for num in row]  
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    for row in matrix:
        # join the numbers in the row with spaces, nicely aligned
        row_text = "  ".join(f"{num:>4}" for num in row)
        print(row_text)


def transpose_matrix(matrix, rows, cols):
    
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(0)
        result.append(new_row)

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b, rows, cols):
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b, m, n, p):
    
    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            new_row.append(0)
        result.append(new_row)

    
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total = total + matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


def part_a_transpose():
    print("\n--- PART A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    transposed = transpose_matrix(matrix, rows, cols)
    print("\nTransposed Matrix:")
    display_matrix(transposed)


def part_b_addition():
    print("\n--- PART B: Add Two Matrices ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix_a = read_matrix(rows, cols, label="first")
    matrix_b = read_matrix(rows, cols, label="second")

    result = add_matrices(matrix_a, matrix_b, rows, cols)

    print("\nSum of Matrices:")
    display_matrix(result)


def part_c_multiplication():
    print("\n--- PART C: Multiply Two Matrices ---")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))

    matrix_a = read_matrix(m, n, label="A")
    matrix_b = read_matrix(n, p, label="B")

    result = multiply_matrices(matrix_a, matrix_b, m, n, p)

    print("\nProduct Matrix (A x B):")
    display_matrix(result)


def main():
    part_a_transpose()
    part_b_addition()
    part_c_multiplication()


main()