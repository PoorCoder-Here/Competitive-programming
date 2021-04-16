#nums=[3,2,1,0,4]
nums=[4,6,8,0,4,3,3,0,1,3,4,5,6,7]
nums1=nums.copy()
d=0
dict={}
strt=0
cov=len(nums)-1
while d<50:
    if cov<=0:
        break
    i=0
    l=[]
    while i<nums[strt]:
        i+=1
        l.append(nums[i+strt])
    dict[nums[strt]]=l
    j=0
    while j<strt:
        nums1[j]=-1
        j+=1
    #print(dict)
    if max(dict[nums[strt]])==0:
        break
    else:
        #print('strt',strt)
        #print(dict)
        #print(nums1)
        cov-=nums1.index(max(dict[nums[strt]]))
        strt=nums1.index(max(dict[nums[strt]]))
    #print(cov)
    #print('d',d)
    d+=1
#print(dict)
#print(cov)
if cov<=0:
    print('True')
else:
    print('False')
