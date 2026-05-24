from math import *

def ktraSoNgTo(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n))):
            if n % i == 0:
                return False
        return True
        
i0 = int(input())
i1 = ktraSoNgTo(i0)
print(i1)
