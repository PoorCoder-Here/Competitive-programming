# passed 11509 test cases
def isPalindrome(x):
        if x<0:
            return "false"
        else:
            ls=[]
            ans=0
            p=0
            tm=x
            while tm>0:
                d=int(tm/10)
                r=tm%10
                ls.append(r)
                tm=d
                p+=1
            j=0
            p=p-1
            while p>=0 or j<p:
                ans+=ls[j]*10**p
                p-=1
                j+=1
            
            if ans==x:
                return "true"
            else:
                return "false"
n=int(input())
print(isPalindrome(n))
