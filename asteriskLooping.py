#Menyusun barisan bintang
for i in range(0,5,1):
    print "*"

#Menyusun barisan bintang dengan nested looping
for i in range(0,5,1):
    output = ''
    for j in range(0,5,1):
        output += '*'
    print output

#Menyusun barisan tangga bintang dengan nested looping
for i in range(1,6,1):
    output = ''
    for j in range(0,i,1):
        output += '*'
    print output

#Menyusun barisan tangga bintang terbalik dengan nested looping
for i in range(0,5,1):
    output = ''
    for j in range(5,i,-1):
        output += '*'
    print output