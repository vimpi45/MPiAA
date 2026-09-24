from lab2p2algoritm import calc_min_dist, calc_min_dist_slow, gen_random_point
from time import thread_time

def time_test():

    all_n = [10, 100, 1000]
   
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