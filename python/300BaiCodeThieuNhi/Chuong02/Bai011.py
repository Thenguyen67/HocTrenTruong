"""Bài tập yêu cầu bạn viết một hàm để tính giai thừa của một số
nguyên. Giai thừa của một số nguyên dương n (ký hiệu là n!) là tích
của tất cả các số nguyên dương từ 1 đến n."""

def giaiThua(n0):
    if n0 < 0:
        return 'Error'
    elif n0 == 0 or n0 == 1:
        return 1 
    else:
        return n0 * giaiThua(n0 - 1)
        

try:
    i0 = int(input())
    print(f'{giaiThua(i0)}')
except:
    print('Error')