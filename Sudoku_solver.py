count=0
pos_possibility={}
def row_traverse(board,row):
    j=0
    res_row=[]
    while j<9:
        if board[row][j]!='.':
           res_row.append(board[row][j])
        j+=1
    return res_row

def col_traverse(board,col):
    i=0
    res_col=[]
    while i<9:
        if board[i][col]!='.':
            res_col.append(board[i][col])
        i+=1
    return res_col

def check1(board):
    i=0
    j=0
    res1=[]
    while i<3:
        while j<3:
            if board[i][j]!='.':
                res1.append(board[i][j])
            j+=1
        i+=1
        j=0
    return res1
def check2(board):
    i=0
    j=3
    res1=[]
    while i<3:
        while j<6:
           if board[i][j]!='.':
               res1.append(board[i][j])
           j+=1 
        i+=1
        j=3
    return res1
def check3(board):
    i=0
    j=6
    res1=[]
    while i<3:
        while j<9:
           if board[i][j]!='.':
               res1.append(board[i][j])
           j+=1 
        i+=1
        j=6
    return res1
def check4(board):
    i=3
    j=0
    res1=[]
    while i<6:
        while j<3:
           if board[i][j]!='.':
               res1.append(board[i][j])
           j+=1 
        i+=1
        j=0
    return res1
def check5(board):
    i=3
    j=3
    res1=[]
    while i<6:
        while j<6:
           if board[i][j]!='.':
               res1.append(board[i][j])
           j+=1 
        i+=1
        j=3
    return res1
def check6(board):
    i=3
    j=6
    res1=[]
    while i<6:
        while j<9:
           if board[i][j]!='.':
               res1.append(board[i][j])
           j+=1 
        i+=1
        j=6
    return res1
def check7(board):
    i=6
    j=0
    res1=[]
    while i<9:
        while j<3:
           if board[i][j]!='.':
               res1.append(board[i][j])
           j+=1 
        i+=1
        j=0
    return res1
def check8(board):
    i=6
    j=3
    res1=[]
    while i<9:
        while j<6:
           if board[i][j]!='.':
               res1.append(board[i][j])
           j+=1 
        i+=1
        j=3
    return res1
def check9(board):
    i=6
    j=6
    res1=[]
    while i<9:
        while j<9:
           if board[i][j]!='.':
               res1.append(board[i][j])
           j+=1 
        i+=1
        j=6
    return res1

def check(board):
    res1=check1(board)
    res2=check2(board)
    res3=check3(board)
    res4=check4(board)
    res5=check5(board)
    res6=check6(board)
    res7=check7(board)
    res8=check8(board)
    res9=check9(board)
    nums=['1','2','3','4','5','6','7','8','9']
    check1_pos=[y for y in nums if y not in res1]
    check2_pos=[y for y in nums if y not in res2]
    check3_pos=[y for y in nums if y not in res3]
    check4_pos=[y for y in nums if y not in res4]
    check5_pos=[y for y in nums if y not in res5]
    check6_pos=[y for y in nums if y not in res6]
    check7_pos=[y for y in nums if y not in res7]
    check8_pos=[y for y in nums if y not in res8]
    check9_pos=[y for y in nums if y not in res9]
    print("check1:",check1_pos)
    print("check2:",check2_pos)
    print("check3:",check3_pos)
    print("check4:",check4_pos)
    print("check5:",check5_pos)
    print("check6:",check6_pos)
    print("check7:",check7_pos)
    print("check8:",check8_pos)
    print("check9:",check9_pos)
    return check1_pos,check2_pos,check3_pos,check4_pos,check5_pos,check6_pos,check7_pos,check8_pos,check9_pos

def empty(board):
    dot=[]
    i=0
    j=0
    while i<9:
        while j<9:
            if board[i][j]=='.':
                dot.append([i,j])
            j+=1
        i+=1
        j=0
    return dot

def rerun(check1_pos,check2_pos,check3_pos,check4_pos,check5_pos,check6_pos,check7_pos,check8_pos,check9_pos):
    k=0
    posi=[]
    dot=empty(board)
    l1=0
    l2=0
    l3=0
    l4=0
    l5=0
    l6=0
    l7=0
    l8=0
    l9=0
    for i in dot:
        if i[0]<3 and i[1]<3:
            l1+=1
            ind=str(i[0])+str(i[1])
            row=row_traverse(board,i[0])
            col=col_traverse(board,i[1])
            res=check1(board)
            while k<len(check1_pos):
                el=check1_pos[k]
                if el not in row and el not in col and el not in res:
                    posi.append(el)
                    k+=1
                else:
                    k+=1
            pos_possibility[ind]=posi.copy()
            posi.clear()
            k=0
        elif i[0]<3 and i[1]>=3 and i[1]<6:
            l2+=1
            ind=str(i[0])+str(i[1])
            row=row_traverse(board,i[0])
            col=col_traverse(board,i[1])
            res=check2(board)
            while k<len(check2_pos):
                el=check2_pos[k]
                if el not in row and el not in col and el not in res:
                    posi.append(el)
                    k+=1
                else:
                    k+=1
            pos_possibility[ind]=posi.copy()
            posi.clear()
            k=0
        elif i[0]<3 and i[1]>=6 and i[1]<9:
            l3+=1
            ind=str(i[0])+str(i[1])
            row=row_traverse(board,i[0])
            col=col_traverse(board,i[1])
            res=check3(board)
            while k<len(check3_pos):
                el=check3_pos[k]
                if el not in row and el not in col and el not in res:
                    posi.append(el)
                    k+=1
                else:
                    k+=1
            pos_possibility[ind]=posi.copy()
            posi.clear()
            k=0
        elif i[0]>=3 and i[0]<6 and i[1]<3:
            l4+=1
            ind=str(i[0])+str(i[1])
            row=row_traverse(board,i[0])
            col=col_traverse(board,i[1])
            res=check4(board)
            while k<len(check4_pos):
                el=check4_pos[k]
                if el not in row and el not in col and el not in res:
                    posi.append(el)
                    k+=1
                else:
                    k+=1
            pos_possibility[ind]=posi.copy()
            posi.clear()
            k=0
        elif i[0]>=3 and i[0]<6 and i[1]>=3 and i[1]<6:
            l5+=1
            ind=str(i[0])+str(i[1])
            row=row_traverse(board,i[0])
            col=col_traverse(board,i[1])
            res=check5(board)
            while k<len(check5_pos):
                el=check5_pos[k]
                if el not in row and el not in col and el not in res:
                    posi.append(el)
                    k+=1
                else:
                    k+=1
            pos_possibility[ind]=posi.copy()
            posi.clear()
            k=0
        elif i[0]>=3 and i[0]<6 and i[1]>=6 and i[1]<9:
            l6+=1
            ind=str(i[0])+str(i[1])
            row=row_traverse(board,i[0])
            col=col_traverse(board,i[1])
            res=check6(board)
            while k<len(check6_pos):
                el=check6_pos[k]
                if el not in row and el not in col and el not in res:
                    posi.append(el)
                    k+=1
                else:
                    k+=1
            pos_possibility[ind]=posi.copy()
            posi.clear()
            k=0
        elif i[0]>=6 and i[1]<3:
            l7+=1
            ind=str(i[0])+str(i[1])
            row=row_traverse(board,i[0])
            col=col_traverse(board,i[1])
            res=check7(board)
            while k<len(check7_pos):
                el=check7_pos[k]
                if el not in row and el not in col and el not in res:
                    posi.append(el)
                    k+=1
                else:
                    k+=1
            pos_possibility[ind]=posi.copy()
            posi.clear()
            k=0
        elif i[0]>=6 and i[1]>=3 and i[1]<6:
            l8+=1
            ind=str(i[0])+str(i[1])
            row=row_traverse(board,i[0])
            col=col_traverse(board,i[1])
            res=check8(board)
            while k<len(check8_pos):
                el=check8_pos[k]
                if el not in row and el not in col and el not in res:
                    posi.append(el)
                    k+=1
                else:
                    k+=1
            pos_possibility[ind]=posi.copy()
            posi.clear()
            k=0
        else:
            l9+=1
            ind=str(i[0])+str(i[1])
            row=row_traverse(board,i[0])
            col=col_traverse(board,i[1])
            res=check9(board)
            while k<len(check9_pos):
                el=check9_pos[k]
                if el not in row and el not in col and el not in res:
                    posi.append(el)
                    k+=1
                else:
                    k+=1
            pos_possibility[ind]=posi.copy()
            posi.clear()
            k=0
remove=[]
board=[["2",".","7","6","5",".",".",".","."],[".",".",".",".","3","2",".",".","."],[".","6",".",".","1",".","5","4","2"],[".","1","2",".","6","5",".","9","4"],["9",".",".","3",".",".","6",".","."],["6",".",".",".",".","9","3","8","."],[".",".",".","5","8","1","2","6","."],[".",".","1",".","9","6","4","5","3"],[".",".",".","7",".",".","9","1","."]]
while count<13:
    ck1,ck2,ck3,ck4,ck5,ck6,ck7,ck8,ck9=check(board)
    rerun(ck1,ck2,ck3,ck4,ck5,ck6,ck7,ck8,ck9)
    print(len(pos_possibility))
    for key,value in pos_possibility.items():
        i=int(key[0])
        j=int(key[1])
        if len(value)==1:
            board[i][j]=value[0]
            remove.append(key)
    for t in remove:
        del pos_possibility[t]
    count+=1
    remove.clear()
print(len(pos_possibility))
for key,value in pos_possibility.items():
    print(key,value)
for o in board:
    print(o)

