def seq(n):
    if n == 0:
        return (1)
    elif n == 1:
        return (2)
    else:
        return seq(n-1) + ((seq(n-1)-seq(n-2))+1)

print(seq(7))