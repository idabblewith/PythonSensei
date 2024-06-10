from days.day_054.files.helpers import *


def day_054():
    title("FUNC SPEED DECORATOR")

    def speed_calc_decorator(function):
        def wrapper_func():
            start_time = time.time()
            function()
            end_time = time.time()
            print(f"Ran in {end_time - start_time} seconds")

        return wrapper_func

    @speed_calc_decorator
    def fast_function():
        for i in range(1000000):
            i * i

    @speed_calc_decorator
    def slow_function():
        for i in range(10000000):
            i * i

    fast_function()
    slow_function()
