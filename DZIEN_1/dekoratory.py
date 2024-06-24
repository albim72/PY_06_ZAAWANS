import time

def time_measurement(func):
    def wrapper():
        starttime = time.time()
        func()
        endtime = time.time()
        delta = endtime-starttime
        print(f'function execution time: {delta} s')
    return wrapper

def sleep(func):
    def wrapper():
        time.sleep(3)
        return func()
    return wrapper


@time_measurement
@sleep
def big_list():
    sum([i**5 for i in range(10_000_000)])

big_list()
