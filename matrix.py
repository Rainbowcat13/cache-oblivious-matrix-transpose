class Matrix:
    def __init__(self, array: list[list[int]]):
        if not array:
            raise ValueError('Incorrect matrix')
        self.array = array
        self.n = len(array)
        self.m = len(array[0])
        self.new_matrix = [[0] * self.m for i in range(self.n)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, x)) for x in self.array])
