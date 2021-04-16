def firstMissingPositive(nums) -> int:
        if len(nums)==0:
            return 1
        else:
            num1=[]
            for i in nums:
                if i>0:
                    num1.append(i)
            nums.clear()
            nums=num1.copy()
            nums=list(set(nums))
            nums.sort()
            i=0
            if len(nums)==0:
                return 1
            elif 1 not in nums:
                return 1
            else:
                while i<len(nums)-1:
                    nex=nums[i]+1
                    if nums[i+1]==nex:
                        i+=1
                    else:
                        return nex
                if len(nums)>1:
                    return nums[-1]+1
                else:
                    return nums[0]+1

print(firstMissingPositive([1,1000]))
