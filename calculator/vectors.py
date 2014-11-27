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
        magnitude = magnitude ** (1/2)
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

    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError()
        if len(self) != len(other):
            raise Exception()
        else:
            sum = 0
            for i in range(len(self)):
                sum += self[i] * other[i]
            return sum

    def cross(self, other):
        if not isinstance(other, Vector):
                raise TypeError()
        if len(self) != 3 or len(other) != 3:
            raise Exception()
        else:
            new_values = [self.y * other.z - self.z * other.y,
                          self.z * other.x - self.x * other.z,
                          self.x * other.y - self.y * other.x]
            return Vector(new_values)