from matrix import Matrix


class CacheObliviousMatrix(Matrix):
    def transpose(self):
        self.transpose_piece(0, 0, self.n, self.m)

    def transpose_piece(self, i, j, w, h):
        if w == 1 and h == 1:
            return
        if w > h:
            self.transpose_piece(i, j, w // 2 + w % 2, h)
            self.transpose_piece(i + w // 2, j, w // 2, h)
            for x in range(i, i + w // 2):
                for y in range(j, j + h):
                    self.array[x][y], self.array[x + w // 2 + w % 2][y] = \
                        self.array[x + w // 2 + w % 2][y], self.array[x][y]
        else:
            self.transpose_piece(i, j, w, h // 2 + h % 2)
            self.transpose_piece(i, j + h // 2, w, h // 2)
            for x in range(i, i + w):
                for y in range(j, j + h // 2):
                    self.array[x][y], self.array[x][y + h // 2 + h % 2] = \
                        self.array[x][y + h // 2 + h % 2], self.array[x][y]


a = CacheObliviousMatrix([[int(x) for x in input().split()] for i in range(int(input()))])
a.transpose()
print(a)
