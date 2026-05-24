def powfunc(in0, in1):
    if in0 == 0: return 0
    elif in0 == 1 or in1 == 0: return 1
    else:
        temp0 = 1
        for i in range(1, in1):
            temp0*= in0
        return temp0

i0, i1 = map(int, input().split())
print(f'{powfunc(i0, i1)}')