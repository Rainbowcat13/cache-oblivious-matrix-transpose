class Matrix:
    def __init__(self, array: list[list[int]]):
        if not array:
            raise ValueError('Incorrect matrix')
        self.array = array
        self.n = len(array)
        self.m = len(array[0])

    def __repr__(self):
        return '\n'.join([' '.join(map(str, x)) for x in self.array])
