import unittest

# Problem: Sum all numbers between the smallest to the highest. Numbers a, b are not ordered.


def get_sum2(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


def get_sum(a, b):
    sum_result = 0
    min_num = min(a, b)
    max_num = max(a, b)
    for i in range(min_num, max_num + 1):
        sum_result += i
    return sum_result

class TestGetSum(unittest.TestCase):

    def test_get_sum(self):
        self.assertTrue(get_sum(0, 1) == 1)
        self.assertTrue(get_sum(0, -1) == -1)
        self.assertTrue(get_sum(1, 1) == 1)
        self.assertTrue(get_sum(-1, 2) == 2)
        self.assertTrue(get_sum(0, 5) == 15)
        
    def test_get_sum2(self):
        self.assertTrue(get_sum2(0, 1) == 1)
        self.assertTrue(get_sum2(0, -1) == -1)
        self.assertTrue(get_sum2(1, 1) == 1)
        self.assertTrue(get_sum2(-1, 2) == 2)
        self.assertTrue(get_sum2(0, 5) == 15)

if __name__ == '__main__':
    unittest.main()