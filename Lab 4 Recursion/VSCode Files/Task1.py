def factorial(n):
    if n == 0 or n == 1:
        return (1)
    else:
        return n * factorial(n-1)

def factorialList(n):
    factList = []
    for i in range(1,n+1):
        factList.append(factorial(i))
    return factList


print(factorialList(5))
    
