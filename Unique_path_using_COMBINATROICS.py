# finding unique path using combinatroics
#c(k,n)=n! / k! * (n - k!)
#k is m-1 , n is m-n-2 i.e one minus from m and one minus from n.
def uniquePaths(self, m: int, n: int) -> int:
        total_steps=m+n-2
        init=m-1
        def fact(n):
            t=1
            ans=1
            while t<=n:
                ans*=t
                t+=1
            return ans
        
        down=fact(m-1)
        right=fact(n-1)
        deno=down*right
        num=fact(total_steps)
        return int(num/deno)
