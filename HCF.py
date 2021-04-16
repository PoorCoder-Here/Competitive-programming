def hcf(a,b):
    if a==b:
        return a
    elif a>b:
        return hcf(a-b,b)
    else:
        return hcf(b-a,a)

x,y=map(int,input().split())
ans=hcf(x,y)
print("HCF is:",ans)
