def urutkanAbjad(str):
    arr = list(str)
    output = ''
    for i in arr:
        for j in range(1,len(arr),1):
            if (arr[j-1] > arr[j]):
                [arr[j-1],arr[j]] = [arr[j],arr[j-1]]
    return output.join(arr)

print (urutkanAbjad('hello')); # 'ehllo'
print (urutkanAbjad('truncate')); # 'acenrttu'
print (urutkanAbjad('developer')); # 'deeeloprv'
print (urutkanAbjad('software')); # 'aeforstw'
print (urutkanAbjad('aegis')); # 'aegis'