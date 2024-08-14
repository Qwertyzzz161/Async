import math
import cProfile
import pstats
import io
from memory_profiler import profile

@profile
def find_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def profile_code():
    pr = cProfile.Profile()
    pr.enable()
    number = 3250000
    divisors_list = find_divisors(number)
    print(divisors_list)
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())


profile_code()

