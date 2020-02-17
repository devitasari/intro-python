kata = raw_input('kata: ')
x = 0
o = 0
for i in range(0,len(kata),1):
    if kata[i] == 'o':
        o += 1
    elif kata[i] == 'x':
        x += 1
if x == o:
    print True
else:
    print False
