# release 0
def sorting(array):
    for i in array:
        for j in range(1,len(array),1):
            if (array[j-1]>array[j]):
                [array[j-1], array[j]] = [array[j], array[j-1]]
    return array

print(sorting([ 2, 4, 6, 8, 2, 3 ]))