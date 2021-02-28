import timeit
t = timeit.Timer("get_smallest_number()", "from __main__ import get_smallest_number")


def get_smallest_number():
    a = [-3, -2, 4, 5, 9, 0, -1, -5, 2]
    a.sort()
    print(f"{a[0]}")


print(f"Execution time for nLogn using sort method: {t.timeit(number=1000)}")
