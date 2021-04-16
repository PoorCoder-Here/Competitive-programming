for _ in range(int(input())):
    level=int(input())
    leaves=list(map(int,input().split()))
    check=[]
    for i in range(1,level+1):
        check.append(i)
    i=0
    j=1
    f=0
    while j<level-1:
        if (check[i]+leaves[j]) == leaves[j+1]:
            i+=1
            j+=1
        else:
            f=1
            break
    if f!=1:
        print("Yes")
    else:
        print("No")
