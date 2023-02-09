a = [1,2,6,4,5]

def getSum(aList):
    if not aList:
        return 0
    else:
        return aList[0] + getSum(aList[1:]) 
print (getSum(a))