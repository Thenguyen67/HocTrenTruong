import random

list0 = [random.randint(0, 9999) for i in range(0, 10)]
print(list0)

tong = 0
for i in range(0, len(list0)):
    tong+= list0[i]

print(tong)