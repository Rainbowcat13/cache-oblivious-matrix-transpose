import random
import sys
import time

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


def time_measure(function, data):
    def wrapper():
        start_time = time.time()
        res = function(data)
        return res, time.time() - start_time
    return wrapper


class Tester:
    def __init__(self, tests_number, matrix_size, max_value):
        self.tests_number = tests_number
        self.matrix_size = matrix_size
        self.max_value = max_value

    def generate_test(self):
        return [[random.randint(0, self.max_value)] * self.matrix_size[1] for i in range(self.matrix_size[0])]

    def run(self):
        time_naive, time_cache_oblivious = 0, 0
        for i in range(self.tests_number):
            test_matrix = self.generate_test()
            result_naive = time_measure(run_naive, test_matrix)()
            result_cache_oblivious = time_measure(run_cache_oblivious, test_matrix)()
            if result_naive[0] != result_cache_oblivious[0]:
                print('Error! Wrong result!')
                return -1, -1
            time_naive += result_naive[1]
            time_cache_oblivious += result_cache_oblivious[1]
        print(f'Tests passed successfully.\nNaive solution average time: {round(time_naive / self.tests_number, 3)} ms.'
              f'\nCache oblivious solution average time: {round(time_cache_oblivious / self.tests_number, 3)} ms.')


if __name__ == '__main__':
    Tester(int(sys.argv[1]), (int(sys.argv[2]), int(sys.argv[3])), int(sys.argv[4])).run()
