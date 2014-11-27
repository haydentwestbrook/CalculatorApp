class Matrix:

    def __init__(self, values):
        if isinstance(values, list):
            for row in values:
                if not isinstance(row, list):
                    raise TypeError()
                if len(row) != len(values[0]):
                    raise TypeError()
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
        string = ""
        for row in self:
            for value in row:
                string += str(value) + " "
            string += "\n"
        return string

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError()
        if other.count() != self.count():
            raise TypeError()
        result = Matrix(self.values)
        for i in range(result.rows):
            for j in range(result.cols):
                result[i][j] += other[i][j]
        return result

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError()
        if other.count() != self.count():
            raise TypeError()
        result = Matrix(self.values)
        for i in range(result.rows):
            for j in range(result.cols):
                result[i][j] -= other[i][j]
        return result
