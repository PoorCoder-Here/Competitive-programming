#works for numbers from 1-3999
def intToRoman(num):
        dict={
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M',
            2:'II',
            3:'III',
            30:'XXX',
            300:'CCC',
            3000:'MMM',
            4:'IV',
            40:'XL',
            400:'CD',
            20:'XX',
            200:'CC',
            2000:'MM'
        }
        s=str(num)
        nu=[]
        po=len(s)-1
        i=0
        while i<len(s):
            nu.append(int(s[i])*10**po)
            i+=1
            po-=1
        fin=""
        for i in nu:
            if dict.get(i):
                fin+=dict.get(i)
            elif i==0:
                continue
            else:
                sr=str(i)
                if i==(10**len(sr))-10**(len(sr)-1):
                    fin+=dict.get(10**(len(sr)-1))
                    fin+=dict.get(10**len(sr))
                elif i<=(10**len(sr))-(2*(10**(len(sr)-1))):
                    fin+=dict.get(5*(10**(len(sr)-1)))
                    li=5*(10**(len(sr)-1))
                    while li<i:
                        fin+=dict.get(10**(len(sr)-1))
                        li+=10**(len(sr)-1)
                        
                    
        return(fin)
print(intToRoman(40))
