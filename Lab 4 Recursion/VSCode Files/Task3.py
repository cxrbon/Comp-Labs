def printToN(n):
    if n != 1:
        printToN(n-1)
    print(n)

def squares(n):
    if n != 1:
        squares(n-1)
    print(n**2)

        
def sumSquares(n):
    if n == 1:
        return 1
    else:
        return n**2 +(sumSquares(n-1))

print(sumSquares(4))
