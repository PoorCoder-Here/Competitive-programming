# passed 3999 testcases and works for roman numerals from 1-3999
def romanToInt(s):
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        fin=0
        s+='0'
        i=0
        while i<len(s)-1:
            if s[i]=="X" and s[i+1]=="L":
                fin+=dict.get('L')-dict.get('X')
                i+=2
            elif s[i]=="C" and s[i+1]=="D":
                fin+=dict.get('D')-dict.get('C')
                i+=2
            elif s[i]=="I" and s[i+1]=="V":
                fin+=dict.get('V')-dict.get('I')
                i+=2
            elif s[i]=="I" and s[i+1]=="X":
                fin+=dict.get('X')-dict.get('I')
                i+=2
            elif s[i]=="X" and s[i+1]=="C":
                fin+=dict.get('C')-dict.get('X')
                i+=2
            elif s[i]=="C" and s[i+1]=="M":
                fin+=dict.get('M')-dict.get('C')
                i+=2
            elif s[i]=="I":
                fin+=dict.get('I')
                i+=1
            elif s[i]=="V":
                fin+=dict.get('V')
                i+=1
            elif s[i]=="X":
                fin+=dict.get('X')
                i+=1
            elif s[i]=="L":
                fin+=dict.get('L')
                i+=1
            elif s[i]=="C":
                fin+=dict.get('C')
                i+=1
            elif s[i]=="D":
                fin+=dict.get('D')
                i+=1
            elif s[i]=="M":
                fin+=dict.get('M')
                i+=1
        return(fin)
print(romanToInt("MCIIV"))
