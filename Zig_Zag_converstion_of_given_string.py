def convert(s,numRows):
    dict={}
    s1=""
    for i in range(len(s)):
        dict[i]=s[i]
    l=0
    lch1=0
    lch=0
    ch=0
    counter=0
    while numRows>1:
          i=numRows+numRows-1-1
          while l<len(s):
                if lch1==lch:
                    s1+=dict.get(l)
                    lch+=1
                    ch+=1
                    dict.pop(l)
                                
                elif ch>=2 and counter>0:
                    l+=counter
                    if l<len(s):
                        s1+=dict.get(l)
                        ch=1
                        dict.pop(l)
    
                else:
                    l=l+i
                    if l<=len(s)-1:
                        s1+=dict.get(l)
                        ch+=1
                        dict.pop(l)
          numRows-=1
          ch=0
          lch1+=1
          l=lch
          counter+=2
    for value in dict.values():
        s1+=value
    return(s1)
print(convert("PAYPALISHIRING",4))
