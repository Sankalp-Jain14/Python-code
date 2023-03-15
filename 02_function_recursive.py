n = int(input())


def factorial_recursive(nf):
    if nf == 1 or nf==0:
        return 1
    return nf* factorial_recursive(nf-1)


f = factorial_recursive(n)
print(f)



