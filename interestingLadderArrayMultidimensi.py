def ladder(word):
    output = []
    for i in range(len(word)):
        raw = []
        for j in range(len(word)-i):
            raw.append(word[j])
        output.append(raw)
    return output

print(ladder('hacktiv8'))