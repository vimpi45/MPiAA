from time import thread_time

nes = [100, 1000, 10000, 100000]

def bench(test, bench_test):
    for n in nes:
        stato = thread_time()
        bench_test(n)
        t_end = (thread_time() - stato)
        print(f"n={n} {test} time = {(t_end)}")
    print("\n")
    
ss = dict()

def list_append(n):
    s = list()
    for i in range(n):
        s.append(i)
    ss[n] = s

def list_insert(n):
    s = ss[n]
    for i in range(n):
        s.insert(0, i)

def list_find(n):
    s = ss[n]
    find_test = list(range(int(100000)))
    for i in find_test:
        if i in s: pass

bench("list append", list_append)
bench("list insert", list_insert)
bench("list find", list_find)