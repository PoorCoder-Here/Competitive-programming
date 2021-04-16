class Solution:
    def countAndSay(self, n: int) -> str:
        dict={1:'1',
             2:'11',
             3:'21',
             4:'1211',
             5:'111221'}
        st=['111221']
        num=['1','2','3','4','5','6','7','8','9']
        inc=5
        while inc<=30:
            s=st[-1]
            i=0
            c=0
            new=""
            while i<len(s):
                if s[i]=='1':
                    c+=1
                    i+=1
                    try:
                        while s[i]=='1':
                            c+=1
                            i+=1
                        new+=str(c)+'1'
                        c=0
                    except:
                        new+=str(c)+'1'
                elif s[i]=='2':
                    c+=1
                    i+=1
                    try:
                        while s[i]=='2':
                            c+=1
                            i+=1
                        new+=str(c)+'2'
                        c=0
                    except:
                        new+=str(c)+'2'
                elif s[i]=='3':
                    c+=1
                    i+=1
                    try:
                        while s[i]=='3':
                            c+=1
                            i+=1
                        new+=str(c)+'3'
                        c=0
                    except:
                        new+=str(c)+'3'
                elif s[i]=='4':
                    c+=1
                    i+=1
                    try:
                        while s[i]=='4':
                            c+=1
                            i+=1
                        new+=str(c)+'4'
                        c=0
                    except:
                        new+=str(c)+'4'
                elif s[i]=='5':
                    c+=1
                    i+=1
                    try:
                        while s[i]=='5':
                            c+=1
                            i+=1
                        new+=str(c)+'5'
                        c=0
                    except:
                        new+=str(c)+'5'
                elif s[i]=='6':
                    c+=1
                    i+=1
                    try:
                        while s[i]=='6':
                            c+=1
                            i+=1
                        new+=str(c)+'6'
                        c=0
                    except:
                        new+=str(c)+'6'
                elif s[i]=='7':
                    c+=1
                    i+=1
                    try:
                        while s[i]=='7':
                            c+=1
                            i+=1
                        new+=str(c)+'7'
                        c=0
                    except:
                        new+=str(c)+'7'
                elif s[i]=='8':
                    c+=1
                    i+=1
                    try:
                        while s[i]=='8':
                            c+=1
                            i+=1
                        new+=str(c)+'8'
                        c=0
                    except:
                        new+=str(c)+'8'
                elif s[i]=='9':
                    c+=1
                    i+=1
                    try:
                        while s[i]=='9':
                            c+=1
                            i+=1
                        new+=str(c)+'9'
                        c=0
                    except:
                        new+=str(c)+'9'
            st.append(new)
            inc+=1
        st.remove('111221')
        q=6
        for i in st:
            dict[q]=i
            q+=1
       
        return dict[n]
