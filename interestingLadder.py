kata = 'hacktiv8'
for i in range(0,len(kata),1):
    output = ''
    x = 1
    for j in range(0,len(kata),1):
        if j<len(kata)-i-1:
            output += ' '
        else:
            if i%2!=len(kata)%2:
                output += kata[j]
            else:
                output += kata[len(kata)-x]
                x += 1
    print output
