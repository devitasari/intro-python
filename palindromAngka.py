angka = 81
isPalindrom = False
while (not isPalindrom):
    angka += 1
    strAngka = str(angka)
    reversedAngka = ''
    for i in range(len(strAngka)-1,-1,-1):
        reversedAngka += strAngka[i]
    if reversedAngka == strAngka:
        isPalindrom = True
        print angka