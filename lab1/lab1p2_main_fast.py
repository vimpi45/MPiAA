import unittest
from random import randint
from lab1p2_fast import has_duplicates_fast, get_duplicates_fast
from time import thread_time

class test_lab(unittest.TestCase):

    def test_has_duplicates_fast(self):
        self.assertEqual(has_duplicates_fast([]), False)
        self.assertEqual(has_duplicates_fast([1]), False)
        self.assertEqual(has_duplicates_fast([2, 1, -4, 7]), False)
        self.assertEqual(has_duplicates_fast([2, -3, 0, 2, 7, 1]), True)
        self.assertEqual(has_duplicates_fast([2, -3, 0, 2, 1, -3, 4, 1, -1, 2]), True)
        self.assertEqual(has_duplicates_fast([4, 4, 4, 4]), True)

    def test_get_duplicates_fast(self):
        self.assertEqual(get_duplicates_fast([]), [])
        self.assertEqual(get_duplicates_fast([1]), [])
        self.assertEqual(get_duplicates_fast([2, 1, -4, 7]), [])
        self.assertEqual(get_duplicates_fast([2, -3, 0, 2, 7, 1]), [2])
        self.assertEqual(get_duplicates_fast([2, -3, 0, 2, 1, -3, 4, 1, -1, 2]), [1, 2, -3])
        self.assertEqual(get_duplicates_fast([4, 4, 4, 4]), [4])


def time_test():
    
    all_n = [100, 1000, 10000, 20000]
    res_has_duplicates = dict()
    res_get_duplicates = dict()

    for n in all_n:
        l = [ randint(0, 100) for i in range(n) ]
        stato = thread_time()
        has_duplicates_fast(l)
        t_end = (thread_time() - stato)

        res_has_duplicates[n] = t_end

    for n in all_n:
        l = [ randint(0, 100) for i in range(n) ]
        stato = thread_time()
        get_duplicates_fast(l)
        t_end = (thread_time() - stato)

        res_get_duplicates[n] = t_end

    for i in all_n:
        print(f'has_duplicates_fast {i} {res_has_duplicates[i]}')

    for i in all_n:
        print(f'get_duplicates_fast {i} {res_get_duplicates[i]}')
        
if __name__ == "__main__":
    # unittest.main()
    time_test()