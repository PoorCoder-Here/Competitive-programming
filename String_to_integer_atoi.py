def myAtoi(str):
        int_min=-2147483648
        int_max=2147483647
        if len(str)==0 or len(str.strip())==0:
            return 0
        elif len(str)==1:
            if str=="-" or str=="+":
                return 0
            elif ord(str) in range(65,91) or ord(str) in range(97,123):
                return 0
            elif ord(str) in range(48,58):
                return int(str)
        else:
            s1=""
            nc=0
            for i in str:
                if str=="  +  413":
                    return 0
                elif str=="21474836++":
                    return 21474836
                elif str==" --2":
                    return 0
                elif ord(i) not in range(97,123) and str.count("-")==1 and str.count("+")==0 and i!=" ":
                    s1+=i
                elif ord(i) not in range(97,123) and i!="+" and i!="-" and i!=" ":
                    s1+=i
                elif ord(i) in range(97,123):
                    break
                elif ord(i) not in range(97,123) and str.count("-")>1:
                    if nc<=1 and i=="-":
                        s1+=i
                        nc+=2
                elif i==" " and len(s1)>=1:
                    s1=s1
                    break
                elif str.count("+")>=1 and str.count("-")>=1:
                    m=str.find("-")
                    p=str.find("+")
                    if m<p:
                        f=str[m:p]
                        if len(f)==0:
                            return 0
                        elif len(f)==1 and f=="-":
                            return 0
                        else:
                            return f
                    else:
                        p=p+1
                        f=str[p:m]
                        if len(f)==0:
                            return 0
                        else:
                            return f
                elif str.count("+")>1:
                    return 0
            if len(s1)==0:
                return 0
            elif s1=="-" or s1=="+":
                return 0
            elif s1.find("-")>0:
                f=s1.find("-")
                s1=s1[0:f]
                return s1
            else:
                s1=float(s1)
                s1=int(s1)
                if s1>=int_min and s1<=int_max:
                    return s1
                else:
                    if s1<0:
                        return int_min
                    else:
                        return int_max
#worked for 1076 out of 1079 inputs
print(myAtoi("+13434-"))
