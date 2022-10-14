import functools
import unittest
import time
from hw2 import _min, _max, _sum, _mult
import functools


class MyTests(unittest.TestCase):
    f = open('test1.txt', 'r')
    sps = list(map(int, f.readline().split()))
    f.close()

    def test_min(self):
        ts = time.perf_counter()
        self.assertEqual(_min(self.sps), min(self.sps))
        print('time_min:', format(time.perf_counter() - ts, '.30f'))

    def test_max(self):
        ts = time.perf_counter()
        self.assertEqual(_max(self.sps), max(self.sps))
        print('time_max:', format(time.perf_counter() - ts, '.30f'))

    def test_sum(self):
        ts = time.perf_counter()
        self.assertEqual(_sum(self.sps), functools.reduce(lambda x, y: x + y, self.sps))
        print('time_sum:', format(time.perf_counter() - ts, '.30f'))


    def test_mult(self):
        ts = time.perf_counter()
        self.assertEqual(_mult(self.sps), functools.reduce(lambda x, y: x * y, self.sps))
        print('time_mult:', format(time.perf_counter() - ts, '.30f'))

    def test_my(self):
        self.assertIs(_min(self.sps), min(self.sps))

    def test_time_program(self):
        ts = time.perf_counter()
        a = _min(self.sps)
        a = _max(self.sps)
        a = _mult(self.sps)
        a = _sum(self.sps)
        self.assertLess(float(format(time.perf_counter() - ts, '.30f')), 0.05)


if __name__ == '__main__':
    unittest.main()


