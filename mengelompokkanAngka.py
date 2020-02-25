def mengelompokkanAngka(arr):
    lipat3 = []
    ganjil = []
    genap = []
    for i in arr:
        if i%3==0:
            lipat3.append(i)
        elif i%2==0:
            genap.append(i)
        else:
            ganjil.append(i)
    return [genap, ganjil, lipat3]

print(mengelompokkanAngka([2, 4, 6])) #[ [2, 4], [], [6] ]
print(mengelompokkanAngka([1, 2, 3, 4, 5, 6, 7, 8, 9])) #[ [ 2, 4, 8 ], [ 1, 5, 7 ], [ 3, 6, 9 ] ]
print(mengelompokkanAngka([100, 151, 122, 99, 111])) #[ [ 100, 122 ], [ 151 ], [ 99, 111 ] ]
print(mengelompokkanAngka([])) #[ [], [], [] ]