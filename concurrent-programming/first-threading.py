import time
import threading

def calculate_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2
    
    print(sum_squares)

def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    start_time = time.time()

    threads = []
    for i in range(5):
        value = (i + 1) * 1000000
        t = threading.Thread(target=calculate_sum_squares, args=(value, ), daemon=False)
        t.start()
        threads.append(t)

    for i in range(len(threads)):
        threads[i].join()
    
    print("Calculating sum of squares took: ", round(time.time() - start_time, 1))

    sleep_start_time = time.time()

    threads = []
    for seconds in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(seconds, ), daemon=False)
        t.start()
        threads.append(t)

    for i in range(len(threads)):
        threads[i].join()
    
    print("Sleep took: ", round(time.time() - sleep_start_time, 1))

if __name__ == "__main__":
    main()