import time
import random

def estimate (func):
    def wrapper (*args) :
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        duration = end_time - start_time
        return f"{func.__name__} tooks {duration} seconds ! and The result is {result}"
    return wrapper


@estimate
def list_create (n):
    n_list = []
    for i in range (n):
        rand_number = random.randrange(n)
        n_list.append(rand_number)
    return n_list

print(list_create(10))