def sittingArrangement(person, column):
    if column == 0:
        return 'Invalid number'
    output = []
    count = 0
    for i in person:
        raw = []
        for j in range(column):
            if count >= len(person):
                raw.append('Kursi Kosong')
            else:
                raw.append(person[count])
            count += 1
        output.append(raw)
        if count >= len(person):
            break
    return output

print(sittingArrangement(['A', 'B', 'C'], 0 )); #Invalid number
print(sittingArrangement([ 'Juli', 'Nisa', 'Desi', 'Ulfa', 'Puji' ], 2)); #[ [ 'Juli', 'Nisa' ], [ 'Desi', 'Ulfa' ], [ 'Puji', 'Kursi Kosong' ] ]
print(sittingArrangement([ 'Yosia', 'Asrawi', 'Andru' ], 3)); #[ [ 'Yosia', 'Asrawi', 'Andru' ] ]
print(sittingArrangement([ 'Lukman', 'Adam', 'Dimas', 'Hansin', 'Orion' ], 4));
# [
#    [ 'Lukman', 'Adam', 'Dimas', 'Hansin' ],
#    [ 'Orion', 'Kursi Kosong', 'Kursi Kosong', 'Kursi Kosong' ]
# ]