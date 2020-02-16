angka = 79918293
strAngka = str(angka)
angkaTerbesar = int(strAngka[0:2])
for i in range(0,len(strAngka),1):
    if (angkaTerbesar < int(strAngka[i:i+2])):
        angkaTerbesar = int(strAngka[i:i+2])

print angkaTerbesar
