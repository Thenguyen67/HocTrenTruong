def tinhTong(n0):
    if n0 < 1:
        print('?')
    tong = int((n0 * (n0 + 1) / 2))
    return tong

i0 = int(input())
print(tinhTong(i0))
