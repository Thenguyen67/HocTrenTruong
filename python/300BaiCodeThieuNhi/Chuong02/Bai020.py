# Chu vi (P) của hình chữ nhật: P = 2 * (dài + rộng)
# Diện tích (A) của hình chữ nhật: A = dài * rộng

def chuVi(d, r): return 2 * (d + r)
def dienTich(d, r): return d * r 

i0, i1 = map(int,input().split())
print(chuVi(i0, i1), dienTich(i0, i1))