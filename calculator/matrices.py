from exceptions import MatrixError

class Matrix:

    def __init__(self, values):
        if isinstance(values, list):
            for row in values:
                if not isinstance(row, list):
                    raise TypeError()
                if len(row) != len(values[0]):
                    raise MatrixError("Each row of the matrix must be the same size.")
            self.values = values
            self.rows = len(values)
            self.cols = len(values[0])
        else:
            raise TypeError()

    def __len__(self):
        return len(self.values)

    def __contains__(self, item):
        for row in self:
            return row.__contains__(item)
        return False

    def __getitem__(self, i):
        return self.values[i]

    def __iter__(self):
        return iter(self.values)

    def count(self):
        count = 0
        for row in self:
            for value in row:
                count += 1
        return count

    def __str__(self):
        max = 0
        for row in self:
            for value in row:
                if abs(value) > max:
                    max = value
        n = len(str(max))
        string = ""
        for row in self:
            for value in row:
                string += str(value) + " " * (n - len(str(value)) + 1)
            string += "\n"
        return string

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError()
        if other.count() != self.count():
            raise MatrixError("Matrices must be the same size.")
        result = Matrix(self.values)
        for i in range(result.rows):
            for j in range(result.cols):
                result[i][j] += other[i][j]
        return result

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError()
        if other.count() != self.count():
            raise MatrixError("Matrices must be the same size.")
        result = Matrix(self.values)
        for i in range(result.rows):
            for j in range(result.cols):
                result[i][j] -= other[i][j]
        return result

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError()
        if not (self.rows == other.cols and self.cols == other.rows):
            raise MatrixError("Matrices were not of compatible sizes.")
        values = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                value = 0
                for k in range(other.rows):
                    value += self[i][k] * other[k][j]
                row.append(value)
            values.append(row)
        return Matrix(values)

    def __div__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError()
        if not (self.rows == other.cols and self.cols == other.rows):
            raise MatrixError("Matrices were not of compatible sizes.")
        values = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                value = 0
                for k in range(other.rows):
                    value += self[i][k] / other[k][j]
                row.append(value)
            values.append(row)
        return Matrix(values)

    def transverse(self):
        values = []
        for i in range(self.cols):
            row = []
            for j in range(self.rows):
                row.append(self[j][i])
            values.append(row)
        return Matrix(values)