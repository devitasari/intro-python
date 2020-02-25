def targetTerdekat(arr):
    x = []
    o = []
    jarak = []
    for i in range(len(arr)):
        if arr[i] == 'o':
            o.append(i)
        elif arr[i] == 'x':
            x.append(i)
    for i in x:
        for j in o:
            jarak.append(abs(i-j))
    jarak.sort()
    if len(jarak) == 0:
        return 0
    return jarak[0]

print(targetTerdekat([' ', ' ', 'o', ' ', ' ', 'x', ' ', 'x'])); # 3
print(targetTerdekat(['o', ' ', ' ', ' ', 'x', 'x', 'x'])); # 4
print(targetTerdekat(['x', ' ', ' ', ' ', 'x', 'x', 'o', ' '])); # 1
print(targetTerdekat([' ', ' ', 'o', ' '])); # 0
print(targetTerdekat([' ', 'o', ' ', 'x', 'x', ' ', ' ', 'x'])); # 2