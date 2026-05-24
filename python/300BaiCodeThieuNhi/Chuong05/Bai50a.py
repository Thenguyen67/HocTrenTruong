myDict1 = {
    'name0' : 'Nguyen The Anh',
    'age0' : 18,
}

myDict2 = {
    'name1' : 'Le Ngoc Mai',
    'age1' : 18,
}

myDict3 = myDict1.copy()
myDict3.update(myDict2)

print(myDict3)