nums=[2,-1,0,1,9,-8,-1,-3,-5,-7,-9,-2,-4,-6,-8,0,-10,-12,-15,-9]
ans=[]
l=len(nums)
i=0
j=1
k=2
while i<l:
    while j<l:
        while k<l:
            ls=[nums[i],nums[j],nums[k]]
            ls.sort()
            s=sum(ls)
            if ls not in ans and s==0:
                ans.append(ls)
            k+=1
        j+=1
        k=j+1
    i+=1
    j=i+1
    k=j+1
print(ans)

            
