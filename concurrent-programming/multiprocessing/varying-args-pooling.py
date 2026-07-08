from multiprocessing import Pool, cpu_count # to adapt to your personal machine

def square(x, y):
    return x**y

num_processes = 4
comparison_list = [1, 2, 3]
power_list = [4, 5, 6]

prepared_list = []
for i in range(len(comparison_list)):
    prepared_list.append((comparison_list[i], power_list[i]))

num_cpu_available = cpu_count() - 1

with Pool(num_cpu_available) as mp_pool:
    result = mp_pool.starmap(square, prepared_list) # [square(1, 4), square(2, 5), square(3, 6)] (x, y) pairs

print(result)