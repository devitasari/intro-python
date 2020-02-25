#Tugas 1
def shotOut():
    print 'Halo Function!'

# shotOut()

#Tugas 2
def calculateMultiply(num1,num2):
    return num1*num2

hasilPerkalian = calculateMultiply(5,6)
# print(hasilPerkalian)

#Tugas 3
def processSentence(name,age,address,hobby):
    return 'Nama saya %s, umur saya %s tahun, alamat saya di %s, dan saya punya hobby yaitu %s' % (name, age, address, hobby)

fullSentence = processSentence('Agus', 30, 'Jl. Malioboro, Yogyakarta', 'gaming')
print fullSentence