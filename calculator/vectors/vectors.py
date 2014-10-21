class vector:

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
        self.magnitude = magnitude

    def add(self, value):
        try:
            int(value)
            self.values.append(value)
        except:
            raise TypeError()

    def __len__(self):
        return len(self.values)

    def __contains__(self, item):
        return self.values.__contains__(item)

    def __add__(self, other):
        if not isinstance(other, vector):
            raise TypeError()
        if len(self) != len(other):
            raise Exception()
        else:
            new_values = []
            for i in range(len(self)):
                new_values.append(self.values[i] + other.values[i])
            return vector(new_values)

    def __sub__(self, other):
        if not isinstance(other, vector):
            raise TypeError()
        if len(self) != len(other):
            raise Exception()
        else:
            new_values = []
            for i in range(len(self)):
                new_values.append(self.values[i] - other.values[i])
            return vector(new_values)

    def __mul__(self, other):
        if not isinstance(other, vector):
            raise TypeError()
        if len(self) != len(other):
            raise Exception()
        else:
            new_values = []
            for i in range(len(self)):
                new_values.append(self.values[i] * other.values[i])
            return vector(new_values)

    def __div__(self, other):
        if not isinstance(other, vector):
            raise TypeError()
        if len(self) != len(other):
            raise Exception()
        else:
            new_values = []
            for i in range(len(self)):
                new_values.append(self.values[i] / other.values[i])
            return vector(new_values)
