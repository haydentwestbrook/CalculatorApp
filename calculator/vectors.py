class Vector:

    def __init__(self, values):
        if isinstance(values, (list, tuple)):
            self.values = values
            if len(values) > 0:
                self.x = values[0]
            if len(values) > 1:
                self.y = values[1]
            if len(values) > 2:
                self.z = values[2]
        else:
            raise TypeError()

    def magnitude(self):
        magnitude = 0
        for value in self.values:
            magnitude += value ** 2
        magnitude ** (1/2)
        return magnitude

    def append(self, value):
        try:
            int(value)
            self.values.append(value)
        except:
            raise TypeError()

    def __len__(self):
        return len(self.values)

    def __contains__(self, item):
        return self.values.__contains__(item)

    def __getitem__(self, i):
        return self.values[i]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return iter(reversed(self.values))

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError()
        if len(self) != len(other):
            raise Exception()
        else:
            new_values = []
            for i in range(len(self)):
                new_values.append(self[i] + other[i])
            return Vector(new_values)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError()
        if len(self) != len(other):
            raise Exception()
        else:
            new_values = []
            for i in range(len(self)):
                new_values.append(self[i] - other[i])
            return Vector(new_values)

    def __mul__(self, other):
        try:
            int(other)
            new_values = []
            for i in range(len(self)):
                new_values.append(self[i] * other)
            return Vector(new_values)
        except:
            raise TypeError()

    def __div__(self, other):
        try:
            int(other)
            new_values = []
            for i in range(len(self)):
                new_values.append(self[i] / other)
            return Vector(new_values)
        except:
            raise TypeError()

    def dot(self, vector_a, vector_b):
        if not isinstance(vector_a, Vector) or not isinstance(vector_b, Vector):
            raise TypeError()
        if len(vector_a) != len(vector_b):
            raise Exception()
        else:
            sum = 0
            for i in range(len(vector_a)):
                sum += vector_a[i] * vector_b[i]
            return sum

    def cross(self, vector_a, vector_b):
        if not isinstance(vector_a, Vector) or not isinstance(vector_b, Vector):
                raise TypeError()
        if len(vector_a) != 3 and len(vector_b) != 3:
            raise Exception()
        else:
            new_values = [vector_a.y * vector_b.z - vector_a.z * vector_b.y,
                          vector_a.z * vector_b.x - vector_a.x * vector_b.z,
                          vector_a.x * vector_b.y - vector_a.y * vector_b.x]
            return Vector(new_values)