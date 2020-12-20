from matrix import Matrix


class NaiveMatrix(Matrix):
    def transpose(self):
        new_matrix = []
        for j in range(self.m):
            cur = []
            for i in range(self.n):
                cur.append(self.array[i][j])
            new_matrix.append(cur)
        self.array = new_matrix
