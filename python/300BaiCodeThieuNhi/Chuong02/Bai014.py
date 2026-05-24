def maxArr(ar):
    max = ar[0]
    for i in range(len(ar) - 1):
        if ar[i] < ar[i+1]:
            max = ar[i+1]
    return max
        

try:
    arr = [int(i) for i in input().split()]
    if not arr:
        print(False)
    else:
        i0 = maxArr(arr)
        print(i0)
except ValueError:
    print('?')
