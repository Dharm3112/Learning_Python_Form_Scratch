import time
# from turtledemo.penrose import start


def timing(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timing
def hello_world(n):
    time.sleep(n)

hello_world(2)