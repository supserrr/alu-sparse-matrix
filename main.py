import sys
from sparse_matrix import SparseMatrix

def perform_operation(op):
    matrix1 = SparseMatrix("sample_inputs/easy_sample_03_1.txt")
    matrix2 = SparseMatrix("sample_inputs/easy_sample_03_2.txt")
    
    # Print dimensions to help with debugging
    print(f"Matrix 1 dimensions: {matrix1.rows}x{matrix1.cols}")
    print(f"Matrix 2 dimensions: {matrix2.rows}x{matrix2.cols}")

    if op == "add":
        result = matrix1.add(matrix2)
    elif op == "subtract":
        result = matrix1.subtract(matrix2)
    elif op == "multiply":
        def show_progress(progress):
            print(f"Multiplication progress: {progress * 100:.2f}%")
            
        # For matrix multiplication, we need to transpose the second matrix if both have the same dimensions
        if matrix1.cols != matrix2.rows and matrix1.cols == matrix2.cols:
            print("Transposing second matrix to make dimensions compatible for multiplication...")
            matrix2 = matrix2.transpose()
            print(f"After transpose, Matrix 2 dimensions: {matrix2.rows}x{matrix2.cols}")
            
        result = matrix1.multiply(matrix2, show_progress)
    else:
        print("Invalid operation")
        return

    with open("results.txt", "w") as f:
        f.write(str(result))
    print("Results have been saved to results.txt")

if __name__ == "__main__":
    operation = input("Select operation (add/subtract/multiply): ").strip().lower()
    perform_operation(operation)
