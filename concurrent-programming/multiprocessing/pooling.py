from multiprocessing import Pool, cpu_count # to adapt to your personal machine
from functools import partial

def square(y, addition, x):
    return x**y + addition

num_processes = 4
comparison_list = [1, 2, 3]
power = 3
addition = 2
num_cpu_available = cpu_count() - 1

partial_function = partial(square, power, addition) # we get a partial function which we then add to result and add comparison_list argument to it
# this way we can have pool mapping with multiple arguments

with Pool(num_cpu_available) as mp_pool:
    result = mp_pool.map(partial_function, comparison_list) # added here partial_function instead of square (can think of it like a pipeline)

print(result)