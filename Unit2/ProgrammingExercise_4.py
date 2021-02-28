import timeit
t = timeit.Timer("get_smallest_number()", "from __main__ import get_smallest_number")


def get_smallest_number():
    a = [-3, -2, 4, 5, 9, 0, -1, -5, 2]
    smallest_number = a[0]
    for index in range(len(a)-1):
        if smallest_number > a[index + 1]:
            smallest_number = a[index + 1]
    print(smallest_number)


print(f"Execution time for a linear method solution: {t.timeit(number=1000)}")
