print "Bilangan faktor 2"
for i in range(1,101,1):
    if i % 2 == 0:
        print str(i)+" - genap"
    else:
        print str(i)+" - ganjil"

print "Bilangan faktor 3"
for i in range(50,2001,5):
    if i % 3 == 0:
        print str(i)+" - faktor 3"
    else:
        print str(i)+" - tidak bisa dibagi 3"

print "Bilangn faktor 8"
for i in range(100,201,7):
    if i % 8 == 0:
        print i