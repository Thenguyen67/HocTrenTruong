def splitToSum(n):
    b = 0
    while n > 0:
        c = 0
        c = n % 10 
        n = n // 10
        b = b + c 
    return b 

i = int(input())
print(f'{splitToSum(i)}')
