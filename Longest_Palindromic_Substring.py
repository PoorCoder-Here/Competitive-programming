def longestPalindrome(s: str) -> str:
        def middle(s,strt,end):
            if len(s)==0 or strt>end:
                return 0
            while strt>=0 and end<len(s) and s[strt]==s[end]:
                strt-=1
                end+=1
            return end-strt+1
        i=0
        st=0
        end=0
        while i<len(s):
            l=max(middle(s,i,i),middle(s,i,i+1))
            if l>end-st:
                st=i-(int((l-1)/2))
                end=i+(int(l/2))
            i+=1
        return(s[st+1:end])

print(longestPalindrome("babad"))
