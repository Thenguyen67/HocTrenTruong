#Viết chương trình để tìm số lớn nhất trong ba số.
x, y, z = map(int, input().split())

if x > y and x > z : print(x)
elif y > z : print(y)
else : print(z)