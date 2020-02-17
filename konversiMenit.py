detik = input("detik: ")
menit = detik / 60
sisa = detik % 60

if sisa < 10:
    print "%s:0%s" %(menit,sisa)
else:
    print "%s:%s" %(menit,sisa)