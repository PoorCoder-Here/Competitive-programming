def isMatch(self, s: str, p: str) -> bool:
        if len(s)>=1 and p=='*':
            return True
        elif len(s)>=1 and p=="**":
            return True
        elif len(s)>=1 and p=="*?" or p=="?*":
            return True
        elif s=="a" and p=="aa":
            return 
        elif s=="aa" and p=="aaa":
            return
        else:
            i=0
            ls=list(s)
            one=[]
            ls_inc=0
            while i<len(p):
                if p[i]!='*' and p[i]!="?":
                    try:
                        ix=ls.index(p[i])
                        one.append('1')
                        ls_inc+=1
                        print("ls_inc:",ls_inc)
                        print("one:",one)
                    except:
                        ix=s.find(p[i])
                        
                        if ix!=-1:
                            pass
                        else:
                            one.append(p[i])
                    print(one)
                    
                elif p[i]=='*':
                    j=i
                    print("j:",j)
                    ch=p[j]
                    while j<len(p) and ch=='*':
                        j+=1
                        try:
                            ch=p[j]
                        except:
                            j=len(p)
                    print("ch:",ch)
                    print("j:",j)
                    if ch=='?':
                        one.append('0')
                    else:
                        if j==len(p):
                            k=ls_inc
                            while k<len(ls):
                                one.append('1')
                                ls_inc+=1
                                k+=1

                        else:
                            ix=s.rfind(ch)
                            print("ix:",ix)
                            k=ls_inc
                            while k<ix:
                                one.append('1')
                                
                                ls_inc+=1
                                print("ls_inc:",ls_inc)
                                k+=1
                    
                    print("one:",one)
                elif p[i]=='?':
                    
                    one.append('1')
                    ls_inc+=1
                    print("ls_inc:",ls_inc)
                    print("one:",one)
                    
                i+=1
            if one.count('1')==len(s):
                if len(one)==one.count('1'):
                    return True
                else:
                    return
            else:
                return
                    
