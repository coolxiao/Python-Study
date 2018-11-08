from collections.abc import Iterable

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[-3:])

P = list(range(100))
print(P[0::5])
print(P)
print(isinstance(P, Iterable))

for i, value in enumerate(P):
    print('index:', i, 'value:', value)
