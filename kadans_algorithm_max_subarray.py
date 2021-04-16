def max_sub(arr):
    max_so_far=0
    max_end=0
    for i in arr:
        max_end=max_end+i
        if max_end<0:
            max_end=0
        elif max_so_far<max_end:
            max_so_far=max_end
    return max_so_far
ls=list(map(int,input().split()))
print(max_sub(ls))
        
