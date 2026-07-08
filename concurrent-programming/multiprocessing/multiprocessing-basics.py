from multiprocessing import Process, Queue
import time

# we divide work into 4 "regions" (because we have 4 processes) to check across
# first would be 0 - 25**6
def check_value_in_list(x, i, num_processes, queue):
    max_number_to_check_to = 10**8
    lower = int(i * max_number_to_check_to / num_processes)
    upper = int((i + 1) * max_number_to_check_to / num_processes)

    number_of_hits = 0

    for i in range(lower, upper):
        if i in x:
            number_of_hits += 1
    
    queue.put((lower, upper, number_of_hits))

num_processes = 4
comparison_list = [1, 2, 3]
queue = Queue()
start_time = time.time()
processes = []
for i in range(num_processes):
    p = Process(target=check_value_in_list, args=(comparison_list, i, num_processes, queue))
    processes.append(p)

for p in processes:
    p.start()

for p in processes:
    p.join()

queue.put('DONE')

while True:
    v = queue.get()
    if v == 'DONE':
        break
    lower, upper, number_of_hits = v
    print('Between ', lower, ' and ', upper, ' we have ', number_of_hits, ' values in the list')

print('Everything took: ', round(time.time() - start_time, 1), 'seconds')