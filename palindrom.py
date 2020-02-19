kata = 'kasur rusak'
reversedKata = ''
for i in range(len(kata)-1,-1,-1):
    reversedKata += kata[i]

if kata == reversedKata:
    print True
else:
    print False