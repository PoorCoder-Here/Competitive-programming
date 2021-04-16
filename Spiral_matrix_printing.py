#matrix=[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36],[37,38,39,40,41,42]]
matrix=[[1,2,3],[4,5,6],[7,8,9 ]]
#matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#matrix=[[1,2],[3,4],[5,6]]
#matrix=[[1,2,3],[2,4,6]]
up=0
down=len(matrix)-1
left=0
right=len(matrix[0])-1
ans=[]
d=0
left_i=1
row_s=len(matrix)
while d<55:
    if up<=down:
        u=matrix[up].copy()
        u=u[left:right+1].copy()
        ans.append(u)
        up+=1
    if right>=left:
        i=up
        while i<=down:
            ans.append(matrix[i][right])
            i+=1
        right-=1
    if down>=up:
        e=matrix[down].copy()
        e=e[left:right+1].copy()
        e=e[::-1].copy()
        ans.append(e)
        down-=1
    if left<=right:
        j=down
        while j>=left_i:
            ans.append(matrix[j][left])
            j-=1
        left_i+=1
        left+=1
    d+=1
ans1=[]
for i in ans:
    if type(i)==list:
        for j in i:
            ans1.append(j)
    else:
        ans1.append(i)
print(ans1)
