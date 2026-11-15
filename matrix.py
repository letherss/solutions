class Matrix:
    def __init__(self, rows):
        if not rows or not rows[0]:
            raise ValueError

        if any(len(row) != len(rows[0]) for row in rows):
            raise ValueError

        self.rows = [row[:] for row in rows]

    @property
    def shape(self):
        return len(self.rows), len(self.rows[0])

    def __getitem__(self, key):
        i, j = key
        return self.rows[i][j]

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError

        return Matrix([
            [self[i, j] + other[i, j] for j in range(self.shape[1])]
            for i in range(self.shape[0])
        ])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([
                [x * other for x in row] for row in self.rows
            ])

        if self.shape[1] != other.shape[0]:
            raise ValueError

        return Matrix([
            [
                sum(self[i, k] * other[k, j] for k in range(self.shape[1]))
                for j in range(other.shape[1])
            ]
            for i in range(self.shape[0])
        ])

    def __rmul__(self, other):
        return self * other

    def transpose(self):
        return Matrix([
            [self[i, j] for i in range(self.shape[0])]
            for j in range(self.shape[1])
        ])

    @classmethod
    def identity(cls, n):
        return cls([
            [1 if i == j else 0 for j in range(n)]
            for i in range(n)
        ])

    def __eq__(self, other):
        return isinstance(other, Matrix) and self.rows == other.rows

    def __repr__(self):
        return f"Matrix({self.rows})"

if __name__ == "__main__":
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[0, 1], [1, 0]])

    print(a.shape)
    print(a[1, 0])
    print(a + b)
    print(a * b)
    print(2 * a)
    print(a * Matrix.identity(2) == a)
    print(Matrix([[1, 2, 3]]).transpose())

    try:
        print(a * Matrix([[1, 2, 3]]))
    except ValueError:
        print("ValueError")