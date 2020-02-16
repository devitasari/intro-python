name = raw_input("name: ")
age = input("age: ")
money = input("money: ")

if name == '':
    print "Anda tidak boleh masuk!"
elif age < 17:
    if money < 50000:
        print "Uang tidak cukup. Anda harus pulang"
    else:
        sisa = money - 50000
        print "Anda bisa pesan jus. Sisa uang anda: Rp %s" % sisa 
else:
    if money < 300000:
        print "Uang tidak cukup. Anda harus pulang"
    else:
        sisa = money - 300000
        print "Anda bisa pesan anggur. Sisa uang anda: Rp %s" % sisa
