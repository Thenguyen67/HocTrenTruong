def checkCharInStr(str, str_Org):
    if str in str_Org:
        return True
    else: return False

i = input()
ii = input()
c = checkCharInStr(ii, i)
if c:
    print(c)