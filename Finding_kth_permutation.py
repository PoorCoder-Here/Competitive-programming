def getPermutation(n: int, k: int):
        res=""
        def perm(n):
            t=1
            a=1
            while t<=n:
                a*=t
                t+=1
            return a
        
        def ini(notinc,n):
            pos=[]
            for i in range(1,n+1):
                if i not in notinc:
                    pos.append(i)
            return pos
        
        def ele(limit,k,pos):
            t=1
            res1=1
            inx=0
            """print("inx",inx)
            while t<=k:
                t=res1*limit
                res1+=1
                if inx<len(pos):
                    inx+=1
                else:
                    inx=0
                print("inx",inx)
            return t,inx-1"""

            while True:
                t=res1*limit
                #print("inx",inx)
                if t<k:
                    res1+=1
                    inx+=1
                    if inx==len(pos):
                        inx=0
                else:
                    break
            return t,inx
        
        r=1
        p=perm(n)
        t_n=n
        while r<=t_n-2:
            notincl=[]
            for j in range(1,t_n+1):
                if str(j) in res:
                    notincl.append(int(j))
            pos=ini(notincl,t_n)
            limit=int(p/n)
            q,at=ele(limit,k,pos)
            #print("pos",pos,"limit",limit,"q",q,"at",at,"notincl",notincl)
            res+=str(pos[at])
            p=limit
            n-=1
            r+=1
            #print("p",p,"r",r,"n",n,"res",res)
        #print(res)
        notincl=[]
        for j in range(1,t_n+1):
            if str(j) in res:
                notincl.append(int(j))
        left=ini(notincl,t_n)
        #print("pos",pos,"limit",limit,"q",q,"at",at,"notincl",notincl)
        if k%2==0:
            left=left[::-1]
            for y in left:
                res+=str(y)
        else:
            for y in left:
                res+=str(y)
        print(res)
getPermutation(4,9)
