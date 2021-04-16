#passed 232 out of 313 test cases
import itertools
def threeSum(nums):
        p=list(itertools.permutations(nums,3))
        ans=[]
        for i in p:
            ni=list(i)
            s=sum(ni)
            ni.sort()
            if s==0:
                if  ni not in ans:
                    ans.append(ni)
        return ans
print(threeSum([5,-9,-11,9,9,-4,14,10,-11,1,-13,11,10,14,-3,-3,-4,6,-15,6,6,-13,7,-11,-15,10,-8,13,-14,-12,12,6,-6,8,0,10,-11,-8,-2,-6,8,0,12,3,-9,-6,8,3,-15,0,-6,-1,3,9,-5,-5,4,2,-15,-3,5,13,-11,7,6,-4,2,11,-5,7,12,-11,-15,1,-1,-9,10,-8,1,2,8,11,-14,-4,-3,-12,-2,8,5,-1,-9,-4,-3,-13,-12,-12,-10,-3,6,1,12,3,-3,12,11,11,10]))
