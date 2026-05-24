"""Bài tập yêu cầu bạn viết một chương trình để in tất cả các số
nguyên tố từ 1 đến 100.
- Một số nguyên tố là một số tự nhiên lớn hơn 1, chỉ có hai ước là 1
và chính nó."""

import math

def inSoNguyenTo(arr):
    for i in arr: 
        print(i, end=' ')

def kiemTraSoNguyenTo():
    arr = []
    for i in range(2, 100):
        laSoNguyenTo = True
        for j in range(2, int(math.sqrt(i))):
            if i % j == 0 :
                laSoNguyenTo = False
                break 
        if laSoNguyenTo: 
            arr.append(i)
    return inSoNguyenTo(arr)

kiemTraSoNguyenTo()
