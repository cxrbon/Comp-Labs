def mininmum (aList):
    if len(aList) == 1:
        return aList[0]
    else:
        return min(aList[0],mininmum(aList[1:]))

print(mininmum([8,2,3,4,5]))