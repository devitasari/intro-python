def tabelPerkalian(angka):
    output = []
    if angka == 1:
        return ['1x1']
    for i in range(1,angka):
        if angka%i==0:
            hasil = angka/i
            if hasil >= i:
                output.append('%dx%d' % (i, hasil))
    return output

print(tabelPerkalian(24)) # [ '1x24', '2x12', '3x8', '4x6' ]
print(tabelPerkalian(90)) # [ '1x90', '2x45', '3x30', '5x18', '6x15', '9x10' ]
print(tabelPerkalian(20)) # [ '1x20', '2x10', '4x5']
print(tabelPerkalian(179)) # [ '1x179' ]
print(tabelPerkalian(1)) # [ '1x1' ]