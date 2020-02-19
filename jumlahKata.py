kalimat = ' I have    a  dream'
count = 0
kataKata = []
kata = ''
for i in range(0,len(kalimat),1):
    if kalimat[i] == ' ' and kata != '':
        kataKata.append(kata)
        kata = ''
    elif kalimat[i] != ' ':
        kata += kalimat[i]
if len(kata) != 0:
    kataKata.append(kata)
print kataKata