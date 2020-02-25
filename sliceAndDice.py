def slice(data, start = 0, end = 0):
    if end == 0:
        end = len(data)
    output = []
    startPoint = False
    for i in range(len(data)):
        if i == start:
            startPoint = True
        if i == end:
            startPoint = False
        if startPoint == True:
            output.append(data[i])
    return output


print(slice(['ant', 'bison', 'camel', 'duck', 'elephant'], 2)); # [ 'camel', 'duck', 'elephant' ]
print(slice(['ant', 'bison', 'camel', 'duck', 'elephant'], 2, 4)); # [ 'camel', 'duck' ]
print(slice(['ant', 'bison', 'camel', 'duck', 'elephant'], 1, 5)); # [ 'bison', 'camel', 'duck', 'elephant' ]
print(slice(['ant', 'bison', 'camel', 'duck', 'elephant'])); #[ 'ant', 'bison', 'camel', 'duck', 'elephant' ]
print(slice(['ant', 'bison', 'camel', 'duck', 'elephant'], 20)); #[]