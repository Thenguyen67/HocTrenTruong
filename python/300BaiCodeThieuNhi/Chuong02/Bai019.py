# Chu vi (C) của hình tròn: C = 2 * pi * r
# Diện tích (A) của hình tròn: A = pi * r^2
import math 
def chuVi(n0):
    return 2 * math.pi * n0

def dienTich(fn0):
    return math.pi * fn0**2 

i = float(input())
print(f'{chuVi(i):.4f}, {dienTich(i):.4f}')