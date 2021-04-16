def longestCommonPrefix(strs):
        if len(strs)==1:
            return strs[0]
        elif len(strs)==0:
            return ""
        else:
            dict={}
            dict['lng']=""
            i=0
            order=0
            while i<len(strs)-1:
                fir=strs[i]
                sec=strs[i+1]
                j=0
                ch=""
                l=min(len(fir),len(sec))
                while j<l:
                    if fir[j]==sec[j]:
                        ch+=fir[j]
                        j+=1
                    else:
                        break
                if len(ch)>=1:
                    order+=1
                fr=dict.get('lng')
                k=0
                ch1=""
               
                ul=len(fr)
                
                if fr=="":
                    dict['lng']=ch
                else:
                    q=min(ul,len(ch))
             
                    while k<q:
                        if fr[k]==ch[k]:
                            
                            ch1+=fr[k]
                            k+=1
                    dict['lng']=ch1
                dict['order']=order
                i+=1
            if dict['order']==len(strs)-1:
                return(dict['lng'])
            else:
                return ""
print(longestCommonPrefix(["flow","flower","flint"]))
