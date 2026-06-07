def countSubstring(str, substr):
    count = 0
    for i in range(0, len(str) - len(substr) + 1):
        Slicestr = str[i : i + len(substr)]
        if Slicestr == substr:
            count = count + 1
    return count 

str = input().strip()
substr = input().strip()
rs = countSubstring(str, substr)
print(rs)