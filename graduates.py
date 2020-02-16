nama = raw_input("Inputkan nama: ")
nilai = input("Inputkan nilai: ")
absen = input("Inputkan absen: ")

if nilai >= 70 and absen < 5:
    print nama,"lulus"
else:
    print nama,"tidak lulus"