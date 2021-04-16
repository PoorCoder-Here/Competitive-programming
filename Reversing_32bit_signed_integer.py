def reverse(n):
    ns=str(abs(n))
    if n<0:
        ns1=-1*int(ns[::-1])
    else:
        ns1=int(ns[::-1])
    if ns1 not in range((-1<<32),(1<<32)-1):
        return 0
    return ns1
n=int(input())
print(reverse(n))
