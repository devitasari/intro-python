# release 0
def sorting(array):
    for i in array:
        for j in range(1,len(array),1):
            if (array[j-1]>array[j]):
                [array[j-1], array[j]] = [array[j], array[j-1]]
    return array

# print(sorting([ 2, 4, 6, 8, 2, 3 ]))

#release 1
def sortingByType(array):
    numberList = []
    stringList = []
    boolList = []
    for i in array:
        if type(i) == int:
            numberList.append(i)
        for j in range(len(numberList)):
            if (numberList[j] < numberList[j-1]):
                [numberList[j-1],numberList[j]] =  [numberList[j],numberList[j-1]]
        if type(i) == bool:
            boolList.append(i)
            for j in range(len(boolList)):
                if (boolList[j] < boolList[j-1]):
                    [boolList[j-1],boolList[j]] =  [boolList[j],boolList[j-1]]
        if type(i) == str:
            stringList.append(i)
            for j in range(len(boolList)):
                if (boolList[j] < boolList[j-1]):
                    [boolList[j-1],boolList[j]] =  [boolList[j],boolList[j-1]]
    return [numberList, stringList, boolList]         

# print(sortingByType([ 1, 3, 'array', -45, True, False, 'big' ]))

# release 2
def sortAllClean(array):
    numberList = []
    stringList = []
    boolList = []
    for i in array:
        if not i:
            del i

    for i in array:
        if type(i) == int:
            numberList.append(i)
        for j in range(len(numberList)):
            if (numberList[j] < numberList[j-1]):
                [numberList[j-1],numberList[j]] =  [numberList[j],numberList[j-1]]
        if type(i) == bool:
            boolList.append(i)
            for j in range(len(boolList)):
                if (boolList[j] < boolList[j-1]):
                    [boolList[j-1],boolList[j]] =  [boolList[j],boolList[j-1]]
        if type(i) == str:
            stringList.append(i)
            for j in range(len(boolList)):
                if (boolList[j] < boolList[j-1]):
                    [boolList[j-1],boolList[j]] =  [boolList[j],boolList[j-1]]
    return [numberList, stringList, boolList]         

print(sortAllClean([ 1, 3, 'array', -45, True, False, 'big', None]))
