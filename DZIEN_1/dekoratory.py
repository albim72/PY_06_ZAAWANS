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


print("_________ decorator debug __________")

def debug(func):
    def wrapper(*args):
        print(f'call function: {func.__name__}')
        func(*args)
    return wrapper
# def wrapper(func,*args):
#     print(f'call function: {func.__name__}')
#     func(*args)

@debug
def info(i):
    print(f'code: {i}')

info("hbjefsjfdkl303480423049")

print("_________ dekorator z parametrem __________")

def repeat(n):
    def wrapper(func):
        def inner(*args):
            for i in range(n):
                func(*args)
        return inner
    return wrapper

@repeat(7)
def calc(c,d):
    print(f'result -> {c*d**2}')

calc(2,3)
