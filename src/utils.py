import time
from colorama import Fore, Style


def PrintElapsedTime(func):
    startingTime = time.perf_counter()

    res = func()

    elapsed_time = time.perf_counter() - startingTime
    print(
        f"Elapsed time: {Fore.GREEN}{str(elapsed_time)}{Style.RESET_ALL} seconds")

    return res
