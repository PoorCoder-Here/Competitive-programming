s,p=input().split()
gen=""
s_ind=0
i=0
t=list(s)
if len(s)>1 and len(p)==1:
    print("False")
elif len(s)>1 and p==".*":
    print("True")
elif len(s)>1 and p=="*.":
    print("False")
else:
    while i<len(p):
        #print("p[i]",p[i])
        if p[i]=='.':
            r=t[::-1].copy()
            ind=r.index('!')
            pos=len(t)-ind
            #print("pos",pos)
            gen+=t[pos]
        elif p[i]=='*':
            st=gen[-1]
            if st in s:
                str_ind=t.index(st)
                t[str_ind]='!'
                j=str_ind+1
                while t[j]==st:
                    t[j]='!'
                    j+=1
                end_ind=j-1
                """try:
                    end_ind=t.index(st)
                    t[end_ind]='!'
                except:
                    end_ind=0"""
                diff=end_ind-str_ind
                #print("diff",diff,"end",end_ind,"str",str_ind)
                gen+=st*diff
                #print(t,st)
            else:
                gen=gen[:-2]
        else:
            gen+=p[i]
        i+=1
    if gen==s:
        print("True")
    else:
        print("False")
    #print(gen)
        
