# Sparse Matrix Operations

This program provides functionality for performing arithmetic operations on sparse matrices using a custom-built `SparseMatrix` class. Users can load matrices from files and perform addition, subtraction, or multiplication.

## Installation

1. Ensure Python 3 is installed on your system.
2. Clone this repository or download the source code.
3. Open a terminal and navigate to the project directory.

## Usage

To run the program, execute the following command:

```bash
python3 main.py
```

The program will prompt you to select an operation: add, subtract, or multiply. Enter your choice and follow the instructions.

## Input File Format

Each matrix should be stored in a text file using the following format:

```
rows=<number_of_rows>
cols=<number_of_columns>
(row, column, value)
(row, column, value)
...
```

### Example

```
rows=3
cols=3
(0, 0, 1)
(1, 1, 2)
(2, 2, 3)
```

## Supported Operations

- **Addition**: Performs element-wise addition of two sparse matrices.
- **Subtraction**: Performs element-wise subtraction (first matrix minus second).
- **Multiplication**: Performs matrix multiplication between the two input matrices.

## Output

The result of the chosen operation will be saved to a file named `results.txt`, formatted the same way as the input files.
