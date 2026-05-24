import random

a = tuple(random.randint(-9999, 9999) for i in range(0, 10))
print(a)
b = min(a)
print(b)