import timeit

op_setitem_1 = timeit.Timer("x[4500]='a'", "from __main__ import x")

op_setitem_2 = timeit.Timer("x[80]='b'", "from __main__ import x")

op_getitem_1 = timeit.Timer("x[80]", "from __main__ import x")

op_getitem_2 = timeit.Timer("x.get(80)", "from __main__ import x")

op_getitem_3 = timeit.Timer("x[80]", "from __main__ import x")

x = {j: None for j in range(10000)}


print(op_setitem_1.timeit(number=1000))

print(op_setitem_2.timeit(number=1000))

print(op_getitem_1.timeit(number=1000))

print(op_getitem_2.timeit(number=1000))

print(op_getitem_3.timeit(number=1000))

