def checkNumber(n) :
    if n < 0 : return 'Âm'
    elif n == 0 : return 'không'
    else : return 'Dương'

try :
    n =  int(input())
    rs = checkNumber(n)
    print(rs)
except :
    print('Error')