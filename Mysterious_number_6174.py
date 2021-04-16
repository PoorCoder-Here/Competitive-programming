n=int(input("Enter the four digit number:"))
i=1
while i<=20:
    n1=list(str(n))
    n1.sort()
    n2=n1[::-1].copy()
    n1=int(''.join(n1))
    n2=int(''.join(n2))
    print('n1:',n1)
    print('n2:',n2)
    ans=n2-n1
    n=ans
    print(n)
    i+=1
