import itertools
from datetime import datetime
now = datetime.now()
start_time = now.strftime("%H:%M:%S")

board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
res=[]
board1=board.copy()


def isValidSudoku(board) -> bool:
        res=[]
        flag=1
        def valid(ls):
            if len(ls)==len(set(ls)):
                return True
            else:
                return False

        for i in board:
            for j in i:
                if j!=".":
                    res.append(j)
                
            ans=valid(res)
            if ans==True:
                res.clear()
                continue
            else:
                return False
        res.clear()
        k=0
        l=0
        while k<9:
            while l<9:
                if board[l][k]!=".":
                    res.append(board[l][k])
                
                l+=1
            ans=valid(res)
            if ans==True:
                res.clear()
            else:
                return False
            k+=1
            l=0
        res.clear()
        res1=[]
        count=2
        li=0
        n=0
        while li<9:
            while n<3:
                res1.append(board[li][n])
                n+=1
            if li==count:
                res.append(list(res1))
                res1.clear()
                count+=3
                li+=1
                n=0
            else:
                li+=1
                n=0
        n=3
        count=2
        li=0
        res1.clear()
        while li<9:
            while n<6:
                res1.append(board[li][n])
                n+=1
            if li==count:
                res.append(list(res1))
                res1.clear()
                count+=3
                li+=1
                n=3
            else:
                li+=1
                n=3
        
        n=6
        count=2
        li=0
        res1.clear()
        while li<9:
            while n<9:
                res1.append(board[li][n])
                n+=1
            if li==count:
                res.append(list(res1))
                res1.clear()
                count+=3
                li+=1
                n=6
            else:
                li+=1
                n=6
        res1.clear()
        for i in res:
            for j in i:
                if j!='.':
                    res1.append(j)
            ans=valid(res1)
            if ans==True:
                res1.clear()
                continue
            else:
                return False
        if flag==1:
            return True

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
def block_ele(row,col):
    if row<3 and col<3:
       res=check1(board)
    elif col>=3 and col<6 and row<3:
         res=check2(board)
    elif col>=6 and col<9 and row<3:
         res=check3(board)
    elif row>=3 and row<6 and col<3:
         res=check4(board)
    elif row>=3 and row<6 and col>=3 and col<6:
         res=check5(board)
    elif row>=3 and row<6 and col>=6 and col<9:
         res=check6(board)
    elif row>=6 and col<3:
         res=check7(board)
    elif row>=6 and col>=3 and col<6:
         res=check8(board)
    elif row>=6 and col>=6 and col<9:
         res=check9(board)
    return res

def rot(di):
        l=len(di)-1
        temp=di[0]
        di=di[1:]
        di.append(temp)
        return di


def dict_dict1():
        nums=['1','2','3','4','5','6','7','8','9']
        row=0
        col=0
        dict={}
        dict1={}
        while row<9:
              row_ele=row_traverse(board,row)
              row_pos=[y for y in nums if y not in row_ele]
              dict1[row]=row_pos
              if row==0:
                 i=0
                 ind=[]
                 while i<9:
                       if board[row][i]=='.':
                          ind.append(i)
                       i+=1
                 dict[row]=ind.copy()   
                 row+=1
              elif row==1:
                   i=0
                   ind=[]
                   while i<9:
                         if board[row][i]=='.':
                            ind.append(i)
                         i+=1
                   dict[row]=ind.copy()
                   row+=1
              elif row==2:
                   i=0
                   ind=[]
                   while i<9:
                         if board[row][i]=='.':
                            ind.append(i)
                         i+=1
                   dict[row]=ind.copy()   
                   row+=1
              elif row==3:
                   i=0
                   ind=[]
                   while i<9:
                         if board[row][i]=='.':
                            ind.append(i)
                         i+=1
                   dict[row]=ind.copy()   
                   row+=1
              elif row==4:
                   i=0
                   ind=[]
                   while i<9:
                         if board[row][i]=='.':
                            ind.append(i)
                         i+=1
                   dict[row]=ind.copy()   
                   row+=1
              elif row==5:
                   i=0
                   ind=[]
                   while i<9:
                         if board[row][i]=='.':
                            ind.append(i)
                         i+=1
                   dict[row]=ind.copy()   
                   row+=1
              elif row==6:
                   i=0
                   ind=[]
                   while i<9:
                         if board[row][i]=='.':
                            ind.append(i)
                         i+=1
                   dict[row]=ind.copy()   
                   row+=1
              elif row==7:
                   i=0
                   ind=[]
                   while i<9:
                         if board[row][i]=='.':
                            ind.append(i)
                         i+=1
                   dict[row]=ind.copy()   
                   row+=1
              else:
                   i=0
                   ind=[]
                   while i<9:
                         if board[row][i]=='.':
                            ind.append(i)
                         i+=1
                   dict[row]=ind.copy()   
                   row+=1
        return dict,dict1

def row1(board3,el,pos):
        fill1=el
        i1=0
        ii1=0
        ind1=pos
        row1=[]
        while ii1<len(el): 
                while i1<len(ind1):
                        board3[0][ind1[i1]]=fill1[i1]
                        i1+=1
                ans=isValidSudoku(board3)
                if ans==True:
                        row1.append(el)
                el=rot(el)
                fill1=el
                ii1+=1
                i1=0
        return row1

def row2(board3,el,pos,row1,pos1):
        i=0
        fill2=el
        i2=0
        ii2=0
        ind2=pos
        row2=[]
        while i<len(row1):
                fill1=row1[i]
                i1=0
                ind1=pos1
                while i1<len(fill1):
                        board3[0][ind1[i1]]=fill1[i1]
                        i1+=1
                while ii2<len(el):
                        while i2<len(ind2):
                                board3[1][ind2[i2]]=fill2[i2]
                                i2+=1
                        ans=isValidSudoku(board3)
                        if ans==True:
                                row2.append(el)
                        el=rot(el)
                        fill2=el.copy()
                        ii2+=1
                        i2=0
                i+=1
                ii2=0
        return row2

def row3(board3,el,pos,row2,pos2,row1,pos1):
        i=0
        j=0
        fill3=el
        i3=0
        ii3=0
        ind3=pos
        row3=[]
        while i<len(row1):
                fill1=row1[i]
                i1=0
                ind1=pos1
                while i1<len(fill1):
                        board3[0][ind1[i1]]=fill1[i1]
                        i1+=1
                while j<len(row2):
                        fill2=row2[j]
                        i2=0
                        ind2=pos2
                        while i2<len(fill2):
                                board3[1][ind2[i2]]=fill2[i2]
                                i2+=1
                        while ii3<len(el):
                                while i3<len(ind3):
                                        board3[2][ind3[i3]]=fill3[i3]
                                        i3+=1
                                ans=isValidSudoku(board3)
                                if ans==True:
                                        row3.append(el)
                                el=rot(el)
                                fill3=el.copy()
                                ii3+=1
                                i3=0
                        j+=1
                        ii3=0
                        i3=0
                i+=1
                j=0
                ii3=0
                i3=0
        return row3

def row4(board3,el,pos,row3,pos3,row2,pos2,row1,pos1):
        i=0
        j=0
        k=0
        fill4=el
        i4=0
        ii4=0
        ind4=pos
        row4=[]
        while i<len(row1):
                fill1=row1[i]
                i1=0
                ind1=pos1
                while i1<len(fill1):
                        board3[0][ind1[i1]]=fill1[i1]
                        i1+=1
                while j<len(row2):
                        fill2=row2[j]
                        i2=0
                        ind2=pos2
                        while i2<len(fill2):
                                board3[1][ind2[i2]]=fill2[i2]
                                i2+=1
                        while k<len(row3):
                                fill3=row3[k]
                                i3=0
                                ind3=pos3
                                while i3<len(fill3):
                                        board3[2][ind3[i3]]=fill3[i3]
                                        i3+=1
                                while ii4<len(el):
                                        while i4<len(ind4):
                                                board3[3][ind4[i4]]=fill4[i4]
                                                i4+=1
                                        ans=isValidSudoku(board3)
                                        if ans==True:
                                                row4.append(el)
                                        el=rot(el)
                                        fill4=el.copy()
                                        ii4+=1
                                        i4=0
                                k+=1
                                ii4=0
                                i4=0
                        j+=1
                        k=0
                        ii4=0
                        i4=0
                i+=1
                j=0
                k=0
                ii4=0
                i4=0
        return row4

def row5(board3,el,pos,row4,pos4,row3,pos3,row2,pos2,row1,pos1):
        i=0
        j=0
        k=0
        l=0
        fill5=el
        i5=0
        ii5=0
        ind5=pos
        row5=[]
        while i<len(row1):
                fill1=row1[i]
                i1=0
                ind1=pos1
                while i1<len(fill1):
                        board3[0][ind1[i1]]=fill1[i1]
                        i1+=1
                while j<len(row2):
                        fill2=row2[j]
                        i2=0
                        ind2=pos2
                        while i2<len(fill2):
                                board3[1][ind2[i2]]=fill2[i2]
                                i2+=1
                        while k<len(row3):
                                fill3=row3[k]
                                i3=0
                                ind3=pos3
                                while i3<len(fill3):
                                        board3[2][ind3[i3]]=fill3[i3]
                                        i3+=1
                                while l<len(row4):
                                        fill4=row4[l]
                                        i4=0
                                        ind4=pos4
                                        while i4<len(fill4):
                                                board[3][ind4[i4]]=fill4[i4]
                                                i4+=1
                                        while ii5<len(el):
                                                while i5<len(ind5):
                                                        board3[4][ind5[i5]]=fill5[i5]
                                                        i5+=1
                                                ans=isValidSudoku(board3)
                                                if ans==True:
                                                        row5.append(el)
                                                el=rot(el)
                                                fill5=el.copy()
                                                ii5+=1
                                                i5=0
                                        l+=1
                                        ii5=0
                                        i5=0
                                k+=1
                                l=0
                                ii5=0
                                i5=0
                        j+=1
                        k=0
                        l=0
                        ii5=0
                        i5=0
                i+=1
                j=0
                k=0
                l=0
                ii5=0
                i5=0
        return row5

def row6(board3,el,pos,row5,pos5,row4,pos4,row3,pos3,row2,pos2,row1,pos1):
        i=0
        j=0
        k=0
        l=0
        m=0
        fill6=el
        i6=0
        ii6=0
        ind6=pos
        row6=[]
        while i<len(row1):
                fill1=row1[i]
                i1=0
                ind1=pos1
                while i1<len(fill1):
                        board3[0][ind1[i1]]=fill1[i1]
                        i1+=1
                print("after updating row1")
                for p in board3:
                        print(p)
                while j<len(row2):
                        fill2=row2[j]
                        i2=0
                        ind2=pos2
                        while i2<len(fill2):
                                board3[1][ind2[i2]]=fill2[i2]
                                i2+=1
                        print("after updating row2")
                        for t in board3:
                                print(t)
                        while k<len(row3):
                                fill3=row3[k]
                                i3=0
                                ind3=pos3
                                while i3<len(fill3):
                                        board3[2][ind3[i3]]=fill3[i3]
                                        i3+=1
                                print("after updating row3")
                                for y in board3:
                                        print(y)
                                while l<len(row4):
                                        fill4=row4[l]
                                        i4=0
                                        ind4=pos4
                                        while i4<len(fill4):
                                                board[3][ind4[i4]]=fill4[i4]
                                                i4+=1
                                        print("after updating row4")
                                        for e in board3:
                                                print(e)
                                        while m<len(row5):
                                                fill5=row5[m]
                                                i5=0
                                                ind5=pos5
                                                while i5<len(fill5):
                                                        board3[4][ind5[i5]]=fill5[i5]
                                                        i5+=1
                                                print("after updating row5")
                                                for r in board3:
                                                        print(r)
                                                while ii6<len(el):
                                                        while i6<len(ind6):
                                                                board3[5][ind6[i6]]=fill6[i6]
                                                                i6+=1
                                                        print("after updating row6")
                                                        for z in board3:
                                                                print(z)
                                                        ans=isValidSudoku(board3)
                                                        print(ans)
                                                        if ans==True:
                                                                row6.append(el)
                                                        el=rot(el)
                                                        print("el:",el)
                                                        fill6=el.copy()
                                                        ii6+=1
                                                        i6=0
                                                m+=1
                                                ii6=0
                                                i6=0
                                        l+=1
                                        m=0
                                        ii6=0
                                        i6=0
                                k+=1
                                l=0
                                m=0
                                ii6=0
                                i6=0
                        j+=1
                        k=0
                        l=0
                        m=0
                        ii6=0
                        i6=0
                i+=1
                j=0
                k=0
                l=0
                m=0
                ii6=0
                i6=0
        return row6
                                
                                
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0
u1=0
dic,dic1=dict_dict1()
print(dic,dic1)
row0=row1(board1,dic1[0],dic[0])
print(row0)
row1=row2(board1,dic1[1],dic[1],row0,dic[0])
print(row1)
"""row2=row3(board1,dic1[2],dic[2],row1,dic[1],row0,dic[0])
print(row2)
row3=row4(board1,dic1[3],dic[3],row2,dic[2],row1,dic[1],row0,dic[0])
print(row3)
row4=row5(board1,dic1[4],dic[4],row3,dic[3],row2,dic[2],row1,dic[1],row0,dic[0])
print(row4)
row5=row6(board1,dic1[5],dic[5],row4,dic[4],row3,dic[3],row2,dic[2],row1,dic[1],row0,dic[0])
print(row5)
row2_pos=[]
row3_pos=[]
""while c1<len(dict1[0]):
        fill1=dict1[0]
        i1=0
        ind1=dict[0]
        while i1<len(fill1):
                board[0][ind1[i1]]=fill1[i1]
                i1+=1
        while c2<len(dict1[1]):
                fill2=dict1[1]
                i2=0
                ind2=dict[1]
                while i2<len(fill2):
                        board[1][ind2[i2]]=fill2[i2]
                        i2+=1
                ans=isValidSudoku(board)
                if ans==True:
                        row2_pos.append(dict1[1])
                        print("in true")
                        c2+=1
                else:
                        for t in board:
                                print(t)
                        ans=isValidSudoku(board)
                        print("in else")
                                
                        while ans==False:
                                dict1[1]=rot(dict1[1])
                                print(dict1[1])
                                fill2=dict1[1]
                                i2=0
                                ind2=dict[1]
                                while i2<len(fill2):
                                        board[1][ind2[i2]]=fill2[i2]
                                        i2+=1
                                ans=isValidSudoku(board)
                                print("\n")
                                for o in board:
                                        print(o)
                        if ans==True:
                                row2_pos.append(dict1[1])
                        c2=len(dict1[1])
                while c3<len(dict1[2]):
                        fill3=dict1[2]
                        i3=0
                        ind3=dict[2]
                        while i3<len(fill3):
                                board[2][ind3[i3]]=fill3[i3]
                                i3+=1
                        ans=isValidSudoku(board)
                        if ans==True:
                                row3_pos.append(dict1[2])
                                c3=len(dict1[2])
                        else:
                                for z in board:
                                        print(z)
                                ans=isValidSudoku(board)
                                while ans==False:
                                        dict1[2]=rot(dict1[2])
                                        print(dict1[2])
                                        fill3=dict1[2]
                                        i3=0
                                        ind3=dict[2]
                                        while i3<len(fill3):
                                                board[2][ind3[i3]]=fill[i3]
                                                i3+=1
                                        ans=isValidSudoku(board)
                                        print("\n")
                                        for o in board:
                                                print(o)
                                row3_pos.append(dict1[2])
                                c3=len(dict[2])
                        while c4<len(dict1[3]):
                                fill4=dict1[3]
                                i4=0
                                ind4=dict[3]
                                while i4<len(fill4):
                                        board[3][ind4[i4]]=fill4[i4]
                                        i4+=1
                                ans=isValidSudoku(board)
                                if ans==True:
                                        c4=len(dict1[3])
                                else:
                                        for z in board:
                                                print(z)
                                        ans=isValidSudoku(board)
                                        while ans==False:
                                                dict1[3]=rot(dict1[3])
                                                print(dict1[3])
                                                fill4=dict1[3]
                                                i4=0
                                                ind4=dict[3]
                                                while i4<len(fill4):
                                                        board[3][ind4[i4]]=fill4[i4]
                                                        i4+=1
                                                ans=isValidSudoku(board)
                                                print("\n")
                                                for o in board:
                                                        print(o)
                                        c4=len(dict1[3])
                                while c5<len(dict1[4]):
                                        fill5=dict1[4]
                                        i5=0
                                        ind5=dict[4]
                                        while i5<len(fill5):
                                                board[4][ind5[i5]]=fill5[i5]
                                                i5+=1
                                        ans=isValidSudoku(board)
                                        if ans==True:
                                                c5=len(dict1[4])
                                        else:
                                                for z in board:
                                                        print(z)
                                                ans=isValidSudoku(board)
                                                while ans==False:
                                                        dict1[4]=rot(dict1[4])
                                                        print(dict1[4])
                                                        fill5=dict1[4]
                                                        i5=0
                                                        ind5=dict[4]
                                                        while i5<len(fill5):
                                                                board[4][ind5[i5]]=fill5[i5]
                                                                i5+=1
                                                        ans=isValidSudoku(board)
                                                        print("\n")
                                                        for o in board:
                                                                print(o)
                                                c5=len(dict1[4])
                                        while c6<len(dict1[5]):
                                                fill6=dict1[5]
                                                i6=0
                                                ind6=dict[5]
                                                while i6<len(fill6):
                                                        board[5][ind6[i6]]=fill6[i6]
                                                        i6+=1
                                                ans=isValidSudoku(board)
                                                if ans==True:
                                                        c6=len(dict1[5])
                                                else:
                                                        for z in board:
                                                                print(z)
                                                        ans=isValidSudoku(board)
                                                        count=0
                                                        while ans==False:
                                                                count+=1
                                                                dict1[5]=rot(dict1[5])        
                                                                print(dict1[5])
                                                                fill6=dict1[5]
                                                                i6=0
                                                                ind6=dict[5]
                                                                while i6<len(fill6):
                                                                        board[5][ind6[i6]]=fill6[i6]
                                                                        i6+=1
                                                                ans=isValidSudoku(board)
                                                                print("\n")
                                                                for o in board:
                                                                        print(o)
                                                                if count==len(dict1[5]):
                                                                        print("cant find match")
                                                                        print(row2_pos)
                                                                        print(row3_pos)
                                                                        break
                                                        c6=len(dict1[5])
                                                                
                                        if ans==True:
                                                c5=len(dict1[4])
                                if ans==True:
                                        c4=len(dict1[3])
                        if ans==True:
                                c3=len(dict1[2])
                if ans==True:
                        c2=len(dict1[1])
        if ans==True:
                c1=len(dict1[0])
print("\n")
for o in board:
        print(o)
print("in c1")
while c1<len(r1):
        
        fill1=r1[c1]
        ind1=dict[0]
        i1=0
        while i1<len(fill1):
                board[0][ind1[i1]]=fill1[i1]
                i1+=1
        print("in c2")
        while c2<len(r2):
                
                fill2=r2[c2]
                ind2=dict[1]
                i2=0
                while i2<len(fill2):
                        board[1][ind2[i2]]=fill2[i2]
                        i2+=1
                print("in c3")
                while c3<len(r3):
                        
                        fill3=r3[c3]
                        ind3=dict[2]
                        i3=0
                        while i3<len(fill3):
                                board[2][ind3[i3]]=fill3[i3]
                                i3+=1
                        print("in c4")
                        while c4<len(r4):
                               
                                fill4=r4[c4]
                                ind4=dict[3]
                                i4=0
                                while i4<len(fill4):
                                        board[3][ind4[i4]]=fill4[i4]
                                        i4+=1
                                print("in c5")
                                while c5<len(r5):
                                        
                                        fill5=r5[c5]
                                        ind5=dict[4]
                                        i5=0
                                        while i5<len(fill5):
                                                board[4][ind5[i5]]=fill5[i5]
                                                i5+=1
                                        print("in c6")
                                        while c6<len(r6):
                                                
                                                fill6=r6[c6]
                                                ind6=dict[5]
                                                i6=0
                                                while i6<len(fill6):
                                                        board[5][ind6[i6]]=fill6[i6]
                                                        i6+=1
                                                print("in c7")
                                                while c7<len(r7):
                                                        
                                                        fill7=r7[c7]
                                                        ind7=dict[6]
                                                        i7=0
                                                        while i7<len(fill7):
                                                                board[6][ind7[i7]]=fill7[i7]
                                                                i7+=1
                                                        print("in c8")
                                                        while c8<len(r8):
                                                                
                                                                fill8=r8[c8]
                                                                ind8=dict[7]
                                                                i8=0
                                                                while i8<len(fill8):
                                                                        board[7][ind8[i8]]=fill8[i8]
                                                                        i8+=1
                                                                print("in c9")
                                                                while c9<len(r9):
                                                                        fill9=r9[c9]
                                                                        ind9=dict[8]
                                                                        i9=0
                                                                        while i9<len(fill9):
                                                                                board[8][ind9[i9]]=fill9[i9]
                                                                                i9+=1
                                                                        ans1=isValidSudoku(board)
                                                                        print("\n")
                                                                        for o in board:
                                                                                print(o)
                                                                        if ans1==True:
                                                                                print("Found out the answer hooooooooooooooorayyyyyyyyyyyyyyyyyy")
                                                                                print("Start Time =", start_time)
                                                                                now = datetime.now()
                                                                                end_time = now.strftime("%H:%M:%S")
                                                                                print("End time=",end_time)
                                                                                c9=len(r9)
                                                                        else:
                                                                                c9+=1
                                                                if ans1==True:
                                                                        c8=len(r8)
                                                                else:
                                                                        c8+=1
                                                                        c9=0
                                                        if ans1==True:
                                                                c7=len(r7)
                                                        else:
                                                                c7+=1
                                                                c8=0
                                                                c9=0
                                                if ans1==True:
                                                        c6=len(r6)
                                                else:
                                                        c6+=1
                                                        c7=0
                                                        c8=0
                                                        c9=0
                                        if ans1==True:
                                                c5=len(r5)
                                        else:
                                                c5+=1
                                                c6=0
                                                c7=0
                                                c8=0
                                                c9=0
                                if ans1==True:
                                        c4=len(r4)
                                else:
                                        c4+=1
                                        c5=0
                                        c6=0
                                        c7=0
                                        c8=0
                                        c9=0
                        if ans1==True:
                                c3=len(r3)
                        else:
                                c3+=1
                                c4=0
                                c5=0
                                c6=0
                                c7=0
                                c8=0
                                c9=0
                if ans1==True:
                        c2=len(r2)
                else:
                        c2+=1
                        c3=0
                        c4=0
                        c5=0
                        c6=0
                        c7=0
                        c8=0
                        c9=0
        if ans1==True:
                c1=len(r1)
        else:
                c1+=1
                c2=0
                c3=0
                c4=0
                c5=0
                c6=0
                c7=0
                c8=0
                c9=0
   """                           
                        
          
          

      
