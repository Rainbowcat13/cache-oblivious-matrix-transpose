import random
import sys

from naive_matrix import NaiveMatrix
from cache_oblivious_matrix import CacheObliviousMatrix


def run_naive(test_matrix):
    nvm = NaiveMatrix(test_matrix)
    nvm.transpose()
    return str(nvm)


def run_cache_oblivious(test_matrix):
    com = CacheObliviousMatrix(test_matrix)
    com.transpose()
    return str(com)


class Tester:
    def __init__(self, tests_number, matrix_size, max_value):
        self.tests_number = tests_number
        self.matrix_size = matrix_size
        self.max_value = max_value

    def generate_test(self):
        return [[random.randint(0, self.max_value)] * self.matrix_size[1] for i in range(self.matrix_size[0])]

    def run(self):
        for i in range(self.tests_number):
            test_matrix = self.generate_test()
            result_naive = run_naive(test_matrix)
            result_cache_oblivious = run_cache_oblivious(test_matrix)
            if result_naive != result_cache_oblivious:
                print('Error! Wrong result!')
                return
        print('Tests passed successfully')


if __name__ == '__main__':
    Tester(int(sys.argv[1]), (int(sys.argv[2]), int(sys.argv[3])), int(sys.argv[4])).run()
