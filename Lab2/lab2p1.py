import unittest
from random import randint
from time import thread_time

class test_lab(unittest.TestCase):

    def test_quicksort(self):
        self.assertEqual(quicksort([]), [])
        self.assertEqual(quicksort([1]), [1])
        self.assertEqual(quicksort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(quicksort([4, -5, 1, 0, 3]), [-5, 0, 1, 3, 4])
        self.assertEqual(quicksort([-5, -5, 0, 2, 3, 3, 8]), [-5, -5, 0, 2, 3, 3, 8])
        self.assertEqual(quicksort([4, 2, 4, -1, 0, 3, -1]), [-1, -1, 0, 2, 3, 4, 4])
        self.assertEqual(quicksort([4, -2, 5, 0, 2, 120, 11, 6, -3, -67, 9, -21, 11]), [-67, -21, -3, -2, 0, 2, 4, 5, 6, 9, 11, 11, 120])     


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []
    for item in arr:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            middle.append(item)
        else:
            right.append(item)      
    return quicksort(left) + middle + quicksort(right)

def time_test():
    
    all_n = [100, 1000, 10000, 100000, 1000000]
    res_quicksort = dict()
    res_sorted = dict()

    for n in all_n:
        l = [ randint(0, 100) for i in range(n) ]
        stato1 = thread_time()
        new_l = sorted(l)
        t_end1 = (thread_time() - stato1)
        res_sorted[n] = t_end1

        stato2 = thread_time()
        quicksort(l)
        t_end2 = (thread_time() - stato2)
        res_quicksort[n] = t_end2

   
    for i in all_n:
        print(f'quicksort result {i} {res_quicksort[i]}')

    for i in all_n:
        print(f'sort() result {i} {res_sorted[i]}')

if __name__ == "__main__":
    # unittest.main()
    time_test()