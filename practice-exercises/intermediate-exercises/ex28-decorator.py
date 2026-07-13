import time

def timer(func):
    # parameters ensure decorator can work on any function
    # regardless of how many arguments it takes
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        duration = end_time - start_time
        print(f"Function '{func.__name__}' took {duration:.4f} seconds.")
        return result
    return wrapper

@timer # syntactic sugar for waste_time = timer(waste_time)
def waste_time():
    time.sleep(1.5)

waste_time()