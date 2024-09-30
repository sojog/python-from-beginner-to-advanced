import time

# t0 = time.time()
# print(t0)

# time.sleep(3)
# t1 = time.time()
# print(t1)


def timeit(f):
    def new_func():
        t0 = time.time()
        f()
        t1 = time.time()
        print("Executed in:", t1 - t0, "seconds")
    return new_func

@timeit
def func1():
    time.sleep(2)
    return [i for i in range(100)]

@timeit
def func2():
    time.sleep(5)
    return [i for i in range(10000)]
        
func1()
func2()