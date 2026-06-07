def Mutation_String(str, pos, char):
    l = list(str)
    l[pos] = char
    str = ''.join(l)
    return str

str = input()
pos, char = input().split()
rs = Mutation_String(str, int(pos), char)
print(rs)
