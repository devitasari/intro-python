def tentukanDeretGeometri(arr):
    dividFactor = arr[1] / arr[0]
    isGeo = True
    for i in range(len(arr)-1,0,-1):
        if arr[i]/dividFactor != arr[i-1]:
            isGeo = False
            break
    return isGeo

print(tentukanDeretGeometri([1, 3, 9, 27, 81])) #true
print(tentukanDeretGeometri([2, 4, 8, 16, 32])) #true
print(tentukanDeretGeometri([2, 4, 6, 8])) #false
print(tentukanDeretGeometri([2, 6, 18, 54])) #true
print(tentukanDeretGeometri([1, 2, 3, 4, 7, 9])) #false