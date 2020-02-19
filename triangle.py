num = 3
for i in range(0,num,1):
    display = ''
    for j in range(0,num+i,1):
        if (j<num-1-i):
            display += ' '
        elif (i%2==0 and j%2==0) or (i%2!=0 and j%2!=0):
            display += 'x'
        else:
            display += 'o'
    print display