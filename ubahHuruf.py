kata = 'i love javascript'
vocal = 'aiueo'
output = ''
for i in range(0,len(kata),1):
    isVocal = False
    for j in range(0,len(vocal),1):
        if kata[i] == vocal[j]:
            isVocal = True
    if isVocal == True:
        output += '$'
    else:
        output += kata[i]

print output