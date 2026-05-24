import random

def findMax(arr):
    maxValue = arr[0]
    for i in range(0, len(arr)):
        if maxValue < arr[i]:
            maxValue = arr[i]
    return maxValue

def findMin(arr):
    minValue = arr[0]
    for i in range(0, len(arr)):
        if minValue > arr[i]:
            minValue = arr[i]
    return minValue

arr = [random.randint(-9999, 9999) for i in range(0, 10)]
print(arr)
print(findMax(arr))
print(findMin(arr))