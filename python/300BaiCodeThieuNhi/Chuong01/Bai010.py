"""Bài tập yêu cầu bạn viết một chương trình để tìm ước số chung lớn
nhất (USCLN) của hai số nguyên.
Ước số chung lớn nhất (USCLN) của hai số nguyên a và b là số lớn
nhất chia hết cả hai số a và b."""

def USCLN(N0, N1):
    while N1 != 0:
        N0, N1 = N1, N0 % N1 
    return N0

try:
    I0, I1 = map(int, input().split())
    print(f'USCLN của {I0} và {I1} là {USCLN(I0, I1)}')
except:
    print('Error')

    