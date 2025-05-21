class SparseMatrix:
    def __init__(self, source):
        self.elements = {}
        if isinstance(source, str):
            self.load_from_file(source)
        elif isinstance(source, dict) and 'rows' in source and 'cols' in source:
            self.rows = source['rows']
            self.cols = source['cols']
        else:
            raise ValueError("Invalid input")

    def load_from_file(self, path):
        with open(path, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        if not lines[0].startswith("rows=") or not lines[1].startswith("cols="):
            raise ValueError("Invalid file format")
        self.rows = int(lines[0].split("=")[1])
        self.cols = int(lines[1].split("=")[1])

        for line in lines[2:]:
            if line.startswith("(") and line.endswith(")"):
                row, col, val = map(int, line[1:-1].split(","))
                self.set_element(row, col, val)
            else:
                raise ValueError("Invalid element format")

    def get_element(self, row, col):
        return self.elements.get((row, col), 0)

    def set_element(self, row, col, val):
        if val != 0:
            self.elements[(row, col)] = val
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for addition")
        result = SparseMatrix({'rows': self.rows, 'cols': self.cols})
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.get_element(i, j) + other.get_element(i, j)
                if val:
                    result.set_element(i, j, val)
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions do not match for subtraction")
        result = SparseMatrix({'rows': self.rows, 'cols': self.cols})
        for i in range(self.rows):
            for j in range(self.cols):
                val = self.get_element(i, j) - other.get_element(i, j)
                if val:
                    result.set_element(i, j, val)
        return result

    def transpose(self):
        """Returns the transpose of this matrix."""
        result = SparseMatrix({'rows': self.cols, 'cols': self.rows})
        for (i, j), v in self.elements.items():
            result.set_element(j, i, v)
        return result

    def multiply(self, other, progress_callback=None):
        if self.cols != other.rows:
            raise ValueError(f"Matrix dimensions do not match for multiplication: ({self.rows}x{self.cols}) and ({other.rows}x{other.cols})")
        result = SparseMatrix({'rows': self.rows, 'cols': other.cols})

        # Index columns of other matrix
        col_index = {}
        for (r, c), v in other.elements.items():
            col_index.setdefault(c, {}).update({r: v})

        operations = 0
        total = len(self.elements) * other.cols

        for (i, k), v1 in self.elements.items():
            for j in range(other.cols):
                if k in col_index.get(j, {}):
                    v2 = col_index[j][k]
                    prev = result.get_element(i, j)
                    result.set_element(i, j, prev + v1 * v2)

                operations += 1
                if progress_callback and operations % 1000000 == 0:
                    progress_callback(operations / total)
        return result

    def __str__(self):
        lines = [f"rows={self.rows}", f"cols={self.cols}"]
        for (i, j), v in sorted(self.elements.items()):
            lines.append(f"({i}, {j}, {v})")
        return "\n".join(lines)
