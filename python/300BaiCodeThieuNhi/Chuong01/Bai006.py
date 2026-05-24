def demChanLe(number):
    bienChan = 0
    bienLe = 0
    for i in number:
        if i % 2 == 0 : bienChan+=1
        else : bienLe+=1
    return bienChan, bienLe

try :
    a = input()
    b = [int(num) for num in a.split()]
    bienChan, bienLe = demChanLe(b)
    print(bienChan, bienLe)
except :
    print('Error')
