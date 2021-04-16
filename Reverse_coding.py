t=int(input())
ans=[19,1119,3119,132119]
for _ in range(t):
    n=int(input())
    if n<len(ans):
        print(ans[n-1])
    else:
        while len(ans)!=n:
            s=''
            temp=str(ans[-1])
            temp=list(temp)
            while len(temp)!=0:
                i=temp[0]
                c=temp.count(i)
                s+=str(c)+str(i)
                f=True
                while f:
                    try:
                        temp.remove(i)
                    except:
                        f=False
            #print(s)
            ans.append(int(s))
        print(ans[n-1])
