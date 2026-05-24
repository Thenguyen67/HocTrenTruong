myDict = {
    'name' : 'Nguyen The Anh',
    'age' : 20,
}
print(f'dict original : {myDict}')

keyWantToDel = input()
if keyWantToDel in myDict:
    myDict.pop(keyWantToDel)
print(f'dict after del key : {myDict}')

