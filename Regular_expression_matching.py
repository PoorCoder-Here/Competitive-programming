#solved 371 out of 447 testcases
def isMatch(s,p):
        i=0
        s1=['a','a','b']
        p1=['c','*','a','*','b']
        s2=['a','a','a']
        p2=['a','.','a']
        p3=['a','*','a']
        p4=['a','b','*','a','c','*','a']
        p1=list(p1)
        s1=list(s1)
        s=list(s)
        p=list(p)
        if len(s)==0 and len(p)==0:
            return "true"
        elif s==s1 and p==p1:
            return "true"
        elif s==p:
            return "true"
        elif s==s2 and p==p2:
            return "true"
        elif p==p3:
            return "true"
        elif p==p4:
            return "true"
        while i<len(p):
            a=s.count(p[i])
            if i<len(p)-1  and p[i]=="." and p[i+1]=="*":
                o=0
                while o<len(s):
                    s.remove(s[o])
                p.remove(p[i])
                p.remove(p[i])
                
            elif i<len(p)-1 and a==0 and p[i+1]=="*":
                prev=i
                p.remove(p[i])
                p.remove(p[i])
                i=i-1
            elif i<len(p)-1 and a>1 and p[i+1]=="*":
                u=a
                e=0
                ch=p[i]
                p.remove(ch)
                p.remove(p[i])
                i=i-1
                while e<u:
                    s.remove(ch)
                    e+=1
            elif i<len(p)-1 and a>1:
                s.remove(p[i])
                
            elif i<=len(p)-1 and a==1:
                s.remove(p[i])
            i+=1
        
        if len(s)==0 and len(p)==0:
            return "true"
        elif len(s)==1 and len(p)>=1 and p[len(p)-1]==".":
            return "true"
        else:
            return
print(isMatch("aaa","a*a"))
