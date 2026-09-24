import unittest
from lab2p2algoritm import calc_min_dist, calc_min_dist_slow, gen_random_point
from time import thread_time

# class test_lab(unittest.TestCase):

#     def test_closest_pair(self):
#         self.assertEqual(calc_min_dist([]), [])
#         self.assertEqual(calc_min_dist([1]), [1])
#         self.assertEqual(calc_min_dist([1, 2, 3]), [1, 2, 3])
#         self.assertEqual(calc_min_dist([4, -5, 1, 0, 3]), [-5, 0, 1, 3, 4])
#         self.assertEqual(calc_min_dist([-5, -5, 0, 2, 3, 3, 8]), [-5, -5, 0, 2, 3, 3, 8])
#         self.assertEqual(calc_min_dist([4, 2, 4, -1, 0, 3, -1]), [-1, -1, 0, 2, 3, 4, 4])
#         self.assertEqual(calc_min_dist([4, -2, 5, 0, 2, 120, 11, 6, -3, -67, 9, -21, 11]), [-67, -21, -3, -2, 0, 2, 4, 5, 6, 9, 11, 11, 120])     

#     def test_closest_pair(self):
#         self.assertEqual(calc_min_dist_slow([]), [])
#         self.assertEqual(calc_min_dist_slow([1]), [1])
#         self.assertEqual(calc_min_dist_slow([1, 2, 3]), [1, 2, 3])
#         self.assertEqual(calc_min_dist_slow([4, -5, 1, 0, 3]), [-5, 0, 1, 3, 4])
#         self.assertEqual(calc_min_dist_slow([-5, -5, 0, 2, 3, 3, 8]), [-5, -5, 0, 2, 3, 3, 8])
#         self.assertEqual(calc_min_dist_slow([4, 2, 4, -1, 0, 3, -1]), [-1, -1, 0, 2, 3, 4, 4])
#         self.assertEqual(calc_min_dist_slow([4, -2, 5, 0, 2, 120, 11, 6, -3, -67, 9, -21, 11]), [-67, -21, -3, -2, 0, 2, 4, 5, 6, 9, 11, 11, 120])     
    


def time_test():

    all_n = [10, 100, 1000] #, 10000 #, 100000]
   
    test_closest_pair = dict()
    test_all_comparison = dict()

    for n in all_n:
        p = gen_random_point(n)

        stato = thread_time()
        calc_min_dist(p)
        t_end = (thread_time() - stato)
        test_closest_pair[n] = t_end

        stato = thread_time()
        calc_min_dist_slow(p)
        t_end = (thread_time() - stato)
        test_all_comparison[n] = t_end

    
    for i in all_n:
        print(f'closest_pair-{i} ---> {test_closest_pair[i]}')
    print()

    for i in all_n:
        print(f'all_comparison-{i} ---> {test_all_comparison[i]}')
    print()

    
if __name__ == '__main__':
    time_test()