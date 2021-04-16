# works only for value of m<10 and n<10
# works till the maximum matrix size of 9 * 9
class node:
    def __init__(self,data):
        self.down=None
        self.right=None
        self.val=data

count=0
def recur(q,m,n):
    limit=m*n
    for _ in range(1,limit+1):
        curr=q.val
        a,b=curr.split(',')
        global count
        prev_down=q
        prev_right=q
        i=int(a)
        j=int(b)
        if i==m and j==n:
            count+=1
        else:
            if i+1<=m:
                t=""
                ai=i
                ai+=1
                t+=str(ai)+","+str(j)
                q.down=node(t)
                prev_down=q.down
            if j+1<=n:
                t=""
                aj=j
                aj+=1
                t+=str(i)+","+str(aj)
                q.right=node(t)
                prev_right=q.right

            #print("down",prev_down.val,"right",prev_right.val)
            if prev_down!=q:
                #recur(prev_down,m,n)
                q=prev_down
                #print("in prevdown")
            elif prev_right!=q:
                #recur(prev_right,m,n)
                q=prev_right
                #print("in prevright")


m,n=map(int,input().split())
root=node(str(11))
i=1
j=1
prev_down=None
prev_right=None
if i+1<=m:
    t=""
    ai=i
    ai+=1
    t+=str(ai)+","+str(j)
    root.down=node(t)
    prev_down=root.down
if j+1<=n:
    t=""
    aj=j
    aj+=1
    t+=str(i)+","+str(aj)
    root.right=node(t)
    prev_right=root.right


#print("root",root.val)
#print("down",root.down.val,"right",root.right.val)
#print("prev_down")
recur(prev_down,m,n)
#print("prev_right")
recur(prev_right,m,n)
print(count)

    
        
