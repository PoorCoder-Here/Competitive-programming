x,y=map(int,input().split())
s=max(x,y)
while s>0:
    if s%x==0 and s%y==0:
        break
    s+=1
print(s)
