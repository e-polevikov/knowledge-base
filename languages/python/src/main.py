_cache = dict()

def cache(func):
    def inner(*args):
        value = _cache.get(args, None)

        if value is not None:
            return value
        
        value = func(*args)
        _cache[args] = value
        return value

    return inner


@cache
def fib(n):
    if n <= 1:
        return n
    
    return fib(n - 1) + fib(n - 2)


print(fib(50))
print(_cache)
