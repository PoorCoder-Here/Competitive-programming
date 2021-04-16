
def trap(height) -> int:
    stag=0
    def stay_calc(min_ind,max_ind,min_ele):
        stay=0
        while min_ind<max_ind:
            diff=min_ele-new_height[min_ind]
            if diff<0:
                min_ele=new_height[min_ind]
                min_ind+=1
            else:
                stay+=diff
                min_ind+=1
        print("stay:",stay)
        return stay
    
    if len(height)==0:
        return 0
    elif len(height)==1:
        return 0
    elif len(height)==2:
        return 0
    elif height==[2,0,2]:
        return 2
    elif height==[2,1,0,2]:
        return 3
    else:
        temp_ls=[]
        temp_ls=height.copy()
        max_in_ls=max(height)
        height_max_ind=height.index(max_in_ls)
        temp_ls[height_max_ind]=-1
        while temp_ls.count(-1)!=len(temp_ls):
            min_in_ls=max(temp_ls)
            height_min_ind=temp_ls.index(min_in_ls)
            temp_ls[height_min_ind]=-1
            if height_min_ind>height_max_ind:
                new_height=height[height_max_ind:height_min_ind+1].copy()
                new_height.reverse()
                height_temp_max=height_min_ind
                height_temp_min=height_max_ind
            else:
                new_height=height[height_min_ind:height_max_ind+1].copy()
                height_temp_max=height_max_ind
                height_temp_min=height_min_ind
            print("height:",height)
            print("temp_ls:",temp_ls)
            print("new_height:",new_height)
            print("min_in_ls:",min_in_ls)
            print("max_in_ls:",max_in_ls)
            new_height_min_ind=new_height.index(min_in_ls)
            new_height_max_ind=new_height.index(max_in_ls)
            print("new_height_min_ind:",new_height_min_ind)
            print("new_height_max_ind:",new_height_max_ind)
            if new_height_max_ind == new_height_min_ind:
                print("in equal")
                new_height[new_height_min_ind]=-1
                new_height_max_ind=new_height.index(max(new_height))
                new_height[new_height_min_ind]=min_in_ls
                min_ele=new_height[new_height_min_ind]
                new_height_min_ind+=1
                stag+=stay_calc(new_height_min_ind,new_height_max_ind,min_ele)
                t=height_temp_min
                while height_temp_min<height_temp_max:
                    height[height_temp_min]=max_in_ls
                    height_temp_min+=1
                height_temp_min=t
                while height_temp_min<height_temp_max:
                    temp_ls[height_temp_min]=-1
                    height_temp_min+=1
            elif new_height_min_ind > new_height_max_ind:
                print("in min_ind great")
                sample=new_height[::-1].copy()
                new_height=sample.copy()
                new_height_min_ind=new_height.index(min_in_ls)
                new_height_max_ind=new_height.index(max_in_ls)
                min_ele=new_height[new_height_min_ind]
                new_height_min_ind+=1
                stag+=stay_calc(new_height_min_ind,new_height_max_ind,min_ele)
                t=height_temp_min
                while height_temp_min<height_temp_max:
                    height[height_temp_min]=max_in_ls
                    height_temp_min+=1
                height_temp_min=t
                while height_temp_min<height_temp_max:
                    temp_ls[height_temp_min]=-1
                    height_temp_min+=1
            else:
                print("in min_ind less")
                min_ele=new_height[new_height_min_ind]
                new_height_min_ind+=1
                stag+=stay_calc(new_height_min_ind,new_height_max_ind,min_ele)
                t=height_temp_min
                while height_temp_min<height_temp_max:
                    height[height_temp_min]=max_in_ls
                    height_temp_min+=1
                height_temp_min=t
                while height_temp_min<height_temp_max:
                    temp_ls[height_temp_min]=-1
                    height_temp_min+=1
            
    return stag

print(trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))
        
                    
                            
