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

def set_add(n):
  s = set()
  for i in range(n):
    s.add(i)
  ss[n] = s

def set_find(n):
  s = ss[n]
  for i in range(10000000):
    if i in s: pass

bench("set add", set_add)
bench("set find", set_find)