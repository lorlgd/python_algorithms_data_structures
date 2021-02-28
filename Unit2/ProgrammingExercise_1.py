import timeit

index_op1 = timeit.Timer("x[80]", "from __main__ import x")

index_op2 = timeit.Timer("x[4500]", "from __main__ import x")

x = list(range(10000))
print(index_op1.timeit(number=1000))

print(index_op2.timeit(number=1000))

