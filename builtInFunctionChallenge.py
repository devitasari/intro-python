def antrian(line,person):
    line.append(person)
    return line

# print antrian(['dev','risan','ardi','sofyan'], 'ricky')

def panggilAntrian(line):
    del line[0]
    return line

# print panggilAntrian(['dev','risan','ardi','sofyan'])

def tumpukan(line,title):
    line.insert(0,title)
    return line

# print tumpukan(['dev','risan','ardi','sofyan'], 'ricky')

def ganjilGenap(plat = 0):
    if (plat == 0):
        return 'invalid data'
    if not plat:
        return 'plat tidak ditemukan' 
    newPlat = plat.split(';')
    genap = 0
    ganjil = 0
    for i in newPlat:
        newValue = int(i)
        if newValue%2==0:
            genap += 1
        else:
            ganjil += 1
    return 'plat genap sebanyak %d dan plat ganjil sebanyak %d' %(genap,ganjil)

print(ganjilGenap('2341;3429;864;1309;1276')) #plat genap sebanyak 2 dan plat ganjil sebanyak 3
print(ganjilGenap('2347;3429;1305')) #plat ganjil sebanyak 3 dan plat genap tidak ditemukan
print(ganjilGenap('864;1308;1276;1432')) #plat genap sebanyak 4 dan plat ganjil tidak ditemukan
print(ganjilGenap('')) #plat tidak ditemukan
print(ganjilGenap()) #invalid data