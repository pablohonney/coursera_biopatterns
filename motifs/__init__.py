from time import time


def timeit(method):
    def wrapper(*args, **kwargs):
        start = time()
        result = method(*args, **kwargs)
        # print('%s lasted %s' % (method.__name__, time() - start))
        return result
    return wrapper
