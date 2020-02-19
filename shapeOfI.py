num = 4

for i in range(0,num,1):
    output = ''
    for j in range(0,num,1):
        if (i==0 or i==num-1):
            output += '#'
        else:
            if (j==num/2 and num%2!=0):
                output += '|'
            elif (j==num/2-1 and num%2==0):
                    output += '||'
            else:
                output += ' '
    print output