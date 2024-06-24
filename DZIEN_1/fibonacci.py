def trace(func):
    def wrapper(*args):
        result = func(*args)
        print(f'{func.__name__}({args}) -> {result}')
        return result
    return wrapper

@trace
def fibonacci(n):
    if n in (0,1):
        return n
    return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(11))
