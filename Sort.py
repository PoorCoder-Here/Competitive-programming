from datetime import datetime as dt
def sort1(l,reverse=False):
    n=len(l)
    i=0
    while i<n:
        j=i+1
        s=l[i]
        while j<n:
            if l[j]<s:
                s=l[j]
                ix=j
            j+=1
        l[i],l[ix]=l[ix],l[i]
        i+=1
    if reverse==True:
        l1=l[::-1]
        return l1
    else:
        return l
a=input("Enter numbers to sort:").split()
order=input("ASC or DSC:").lower()
if order=='asc':
    now=dt.now()
    print("seconds:",now.strftime("%f"))
    print(sort1(a))
    now=dt.now()
    print("seconds:",now.strftime("%f"))
else:
    now=dt.now()
    print("seconds:",now.strftime("%f"))
    print(sort1(a,True))
    now=dt.now()
    print("seconds:",now.strftime("%f"))
