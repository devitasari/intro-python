nama = raw_input("Input nama: ")
nilai = input("Input nilai: ")

if nilai >79 and nilai <101:
    print nama,": grade A"
elif nilai >64:
    print nama,": grade B"
elif nilai >49:
    print nama,": grade C"
elif nilai >34:
    print nama,": grade D"
elif nilai >=0:
    print nama,": grade E"
else:
    print "Nilai Invalid"