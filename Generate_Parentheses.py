ans=[]
n=int(input())
def backtrack(s="",l=0,r=0):
    #print("s",s,l,r)
    if len(s)==n*2:
        ans.append(s)
        return
    if l<n:
        #print("left")
        backtrack(s+'(',l+1,r)
    if r<l:
        #print("right")
        backtrack(s+')',l,r+1)
backtrack()
print(ans)
        
