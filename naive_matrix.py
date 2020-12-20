from matrix import Matrix


class NaiveMatrix(Matrix):
    def transpose(self):
        new_matrix = [[0] * self.m for i in range(self.n)]
        for j in range(self.m):
            for i in range(self.n):
                new_matrix[j][i] = self.array[i][j]
        self.array = new_matrix
