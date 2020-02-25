def tukarBesarKecil(kalimat):
    output = ''
    for i in kalimat:
        if i == i.upper():
            output += i.lower()
        else:
            output += i.upper()
    return output

print(tukarBesarKecil('Hello World')); # "hELLO wORLD"
print(tukarBesarKecil('I aM aLAY')); # "i Am Alay"
print(tukarBesarKecil('My Name is Bond!!')); # "mY nAME IS bOND!!"
print(tukarBesarKecil('IT sHOULD bE me')); # "it Should Be ME"
print(tukarBesarKecil('001-A-3-5TrdYW')); # "001-a-3-5tRDyw"
