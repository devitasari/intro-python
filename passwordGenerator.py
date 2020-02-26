def changeVocals(str):
    vocals = 'aiueoAIUEO'
    abjad = 'bjvfpBJVFP'
    output = ''
    for i in range(len(str)):
        add = True
        for j in range(len(vocals)):
            if str[i] == vocals[j]:
                output += abjad[j]
                add = False
        if add:
            output += str[i]
    return output

# print(changeVocals('air'))

def reverseWord(str):
    output = ''
    for i in range(len(str)-1,-1,-1):
        output += str[i]
    return output

# print(reverseWord('air'))

def setLowerUpperCase(str):
    output = ''
    for i in str:
        if i == i.lower():
            output += i.upper()
        else:
            output += i.lower()
    return output

def removeSpaces(str):
    output = ''
    for i in str:
        if i != ' ':
            output += i
    return output

# print(removeSpaces('devita sari'))

def passwordGenerator(name):
    if len(name) < 5:
        return 'Minimal karakter yang diinputkan adalah 5 karakter'
    return removeSpaces(setLowerUpperCase(reverseWord(changeVocals(name))))



print(passwordGenerator('Sergei Dragunov'))# 'VPNVGBRdJFGRFs'
print(passwordGenerator('Dimitri Wahyudiputra'))# 'BRTVPJDVYHBwJRTJMJd'
print(passwordGenerator('Alexei'))# 'JFXFLb'
print(passwordGenerator('Alex'))# 'Minimal karakter yang diinputkan adalah 5 karakter'