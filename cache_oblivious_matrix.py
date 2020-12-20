from matrix import Matrix


class CacheObliviousMatrix(Matrix):
    def transpose(self):
        self.new_matrix = [[-1] * self.m for i in range(self.n)]
        self.transpose_piece(0, 0, self.n, self.m)
        self.array = self.new_matrix

    def transpose_piece(self, i, j, w, h):
        if w <= 75 and h <= 75:
            for x in range(i, i + h):
                for y in range(j, j + w):
                    self.new_matrix[y][x] = self.array[x][y]
            return
        if w >= h:
            whalf = w // 2
            self.transpose_piece(i, j, whalf, h)
            self.transpose_piece(i, j + whalf, w - whalf, h)
        else:
            hhalf = h // 2
            self.transpose_piece(i, j, w, hhalf)
            self.transpose_piece(i + hhalf, j, w, h - hhalf)
