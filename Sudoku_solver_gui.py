from guizero import TextBox,App,PushButton,Text
def solution():
    row1=[]
    row1.append(text1.value)
    row1.append(text2.value)
    row1.append(text3.value)
    row1.append(text4.value)
    row1.append(text5.value)
    row1.append(text6.value)
    row1.append(text7.value)
    row1.append(text8.value)
    row1.append(text9.value)
    print(row1)
    row2=[]
    row2.append(text10.value)
    row2.append(text11.value)
    row2.append(text12.value)
    row2.append(text13.value)
    row2.append(text14.value)
    row2.append(text15.value)
    row2.append(text16.value)
    row2.append(text17.value)
    row2.append(text18.value)
    print(row2)
    row3=[]
    row3.append(text19.value)
    row3.append(text20.value)
    row3.append(text21.value)
    row3.append(text22.value)
    row3.append(text23.value)
    row3.append(text24.value)
    row3.append(text25.value)
    row3.append(text26.value)
    row3.append(text27.value)
    print(row3)
    row4=[]
    row4.append(text28.value)
    row4.append(text29.value)
    row4.append(text30.value)
    row4.append(text31.value)
    row4.append(text32.value)
    row4.append(text33.value)
    row4.append(text34.value)
    row4.append(text35.value)
    row4.append(text36.value)
    print(row4)
    row5=[]
    row5.append(text37.value)
    row5.append(text38.value)
    row5.append(text39.value)
    row5.append(text40.value)
    row5.append(text41.value)
    row5.append(text42.value)
    row5.append(text43.value)
    row5.append(text44.value)
    row5.append(text45.value)
    print(row5)
    row6=[]
    row6.append(text46.value)
    row6.append(text47.value)
    row6.append(text48.value)
    row6.append(text49.value)
    row6.append(text50.value)
    row6.append(text51.value)
    row6.append(text52.value)
    row6.append(text53.value)
    row6.append(text54.value)
    print(row6)
    row7=[]
    row7.append(text55.value)
    row7.append(text56.value)
    row7.append(text57.value)
    row7.append(text58.value)
    row7.append(text59.value)
    row7.append(text60.value)
    row7.append(text61.value)
    row7.append(text62.value)
    row7.append(text63.value)
    print(row7)
    row8=[]
    row8.append(text64.value)
    row8.append(text65.value)
    row8.append(text66.value)
    row8.append(text67.value)
    row8.append(text68.value)
    row8.append(text69.value)
    row8.append(text70.value)
    row8.append(text71.value)
    row8.append(text72.value)
    print(row8)
    row9=[]
    row9.append(text73.value)
    row9.append(text74.value)
    row9.append(text75.value)
    row9.append(text76.value)
    row9.append(text77.value)
    row9.append(text78.value)
    row9.append(text79.value)
    row9.append(text80.value)
    row9.append(text81.value)
    print(row9)
    r1=[text1,text2,text3,text4,text5,text6,text7,text8,text9]
    r2=[text10,text11,text12,text13,text14,text15,text16,text17,text18]
    r3=[text19,text20,text21,text22,text23,text24,text25,text26,text27]
    r4=[text28,text29,text30,text31,text32,text33,text34,text35,text36]
    r5=[text37,text38,text39,text40,text41,text42,text43,text44,text45]
    r6=[text46,text47,text48,text49,text50,text51,text52,text53,text54]
    r7=[text55,text56,text57,text58,text59,text60,text61,text62,text63]
    r8=[text64,text65,text66,text67,text68,text69,text70,text71,text72]
    r9=[text73,text74,text75,text76,text77,text78,text79,text80,text81]


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
    board=[]
    board.append(row1)
    board.append(row2)
    board.append(row3)
    board.append(row4)
    board.append(row5)
    board.append(row6)
    board.append(row7)
    board.append(row8)
    board.append(row9)
    while count<50:
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
    for o in board:
        print(o)

    j=0
    for i in r1:
        i.value=board[0][j]
        i.enabled=False
        j+=1
    j=0
    for i in r2:
        i.value=board[1][j]
        i.enabled=False
        j+=1
    j=0
    for i in r3:
        i.value=board[2][j]
        i.enabled=False
        j+=1
    j=0
    for i in r4:
        i.value=board[3][j]
        i.enabled=False
        j+=1
    j=0
    for i in r5:
        i.value=board[4][j]
        i.enabled=False
        j+=1
    j=0
    for i in r6:
        i.value=board[5][j]
        i.enabled=False
        j+=1
    j=0
    for i in r7:
        i.value=board[6][j]
        i.enabled=False
        j+=1
    j=0
    for i in r8:
        i.value=board[7][j]
        i.enabled=False
        j+=1
    j=0
    for i in r9:
        i.value=board[8][j]
        i.enabled=False
        j+=1
    
    bt.enabled=False
    
app=App(title="Sudoku Solver",height=286,width=790,layout="grid")
i1=Text(app,text="Instructions:",grid=[0,0])
i2=Text(app,text="1.Only fill the boxes",grid=[0,1])
i3=Text(app,text="with number(1-9)",grid=[0,2])
i4=Text(app,text="2.Leave the empty box as it is",grid=[0,3])
i5=Text(app,text="3.Replace the dot with",grid=[0,4])
i6=Text(app,text="number",grid=[0,5])
i7=Text(app,text="4.Don't append the dot",grid=[0,6])
i8=Text(app,text="with number",grid=[0,7])
i9=Text(app,text="5.Strictly follow the",grid=[0,8])
i10=Text(app,text="instuctions for accuracy",grid=[0,9])
i11=Text(app,text="5.Mess with the sudoku :)",grid=[0,10])

text1=TextBox(app,text=".",grid=[1,0])
text2=TextBox(app,text=".",grid=[2,0])
text3=TextBox(app,text=".",grid=[3,0])
text4=TextBox(app,text=".",grid=[4,0])
text5=TextBox(app,text=".",grid=[5,0])
text6=TextBox(app,text=".",grid=[6,0])
text7=TextBox(app,text=".",grid=[7,0])
text8=TextBox(app,text=".",grid=[8,0])
text9=TextBox(app,text=".",grid=[9,0])
text10=TextBox(app,text=".",grid=[1,1])
text11=TextBox(app,text=".",grid=[2,1])
text12=TextBox(app,text=".",grid=[3,1])
text13=TextBox(app,text=".",grid=[4,1])
text14=TextBox(app,text=".",grid=[5,1])
text15=TextBox(app,text=".",grid=[6,1])
text16=TextBox(app,text=".",grid=[7,1])
text17=TextBox(app,text=".",grid=[8,1])
text18=TextBox(app,text=".",grid=[9,1])
text19=TextBox(app,text=".",grid=[1,2])
text20=TextBox(app,text=".",grid=[2,2])
text21=TextBox(app,text=".",grid=[3,2])
text22=TextBox(app,text=".",grid=[4,2])
text23=TextBox(app,text=".",grid=[5,2])
text24=TextBox(app,text=".",grid=[6,2])
text25=TextBox(app,text=".",grid=[7,2])
text26=TextBox(app,text=".",grid=[8,2])
text27=TextBox(app,text=".",grid=[9,2])
text28=TextBox(app,text=".",grid=[1,3])
text29=TextBox(app,text=".",grid=[2,3])
text30=TextBox(app,text=".",grid=[3,3])
text31=TextBox(app,text=".",grid=[4,3])
text32=TextBox(app,text=".",grid=[5,3])
text33=TextBox(app,text=".",grid=[6,3])
text34=TextBox(app,text=".",grid=[7,3])
text35=TextBox(app,text=".",grid=[8,3])
text36=TextBox(app,text=".",grid=[9,3])
text37=TextBox(app,text=".",grid=[1,4])
text38=TextBox(app,text=".",grid=[2,4])
text39=TextBox(app,text=".",grid=[3,4])
text40=TextBox(app,text=".",grid=[4,4])
text41=TextBox(app,text=".",grid=[5,4])
text42=TextBox(app,text=".",grid=[6,4])
text43=TextBox(app,text=".",grid=[7,4])
text44=TextBox(app,text=".",grid=[8,4])
text45=TextBox(app,text=".",grid=[9,4])
text46=TextBox(app,text=".",grid=[1,5])
text47=TextBox(app,text=".",grid=[2,5])
text48=TextBox(app,text=".",grid=[3,5])
text49=TextBox(app,text=".",grid=[4,5])
text50=TextBox(app,text=".",grid=[5,5])
text51=TextBox(app,text=".",grid=[6,5])
text52=TextBox(app,text=".",grid=[7,5])
text53=TextBox(app,text=".",grid=[8,5])
text54=TextBox(app,text=".",grid=[9,5])
text55=TextBox(app,text=".",grid=[1,6])
text56=TextBox(app,text=".",grid=[2,6])
text57=TextBox(app,text=".",grid=[3,6])
text58=TextBox(app,text=".",grid=[4,6])
text59=TextBox(app,text=".",grid=[5,6])
text60=TextBox(app,text=".",grid=[6,6])
text61=TextBox(app,text=".",grid=[7,6])
text62=TextBox(app,text=".",grid=[8,6])
text63=TextBox(app,text=".",grid=[9,6])
text64=TextBox(app,text=".",grid=[1,7])
text65=TextBox(app,text=".",grid=[2,7])
text66=TextBox(app,text=".",grid=[3,7])
text67=TextBox(app,text=".",grid=[4,7])
text68=TextBox(app,text=".",grid=[5,7])
text69=TextBox(app,text=".",grid=[6,7])
text70=TextBox(app,text=".",grid=[7,7])
text71=TextBox(app,text=".",grid=[8,7])
text72=TextBox(app,text=".",grid=[9,7])
text73=TextBox(app,text=".",grid=[1,8])
text74=TextBox(app,text=".",grid=[2,8])
text75=TextBox(app,text=".",grid=[3,8])
text76=TextBox(app,text=".",grid=[4,8])
text77=TextBox(app,text=".",grid=[5,8])
text78=TextBox(app,text=".",grid=[6,8])
text79=TextBox(app,text=".",grid=[7,8])
text80=TextBox(app,text=".",grid=[8,8])
text81=TextBox(app,text=".",grid=[9,8])
bt=PushButton(app,text="Reveal",command=solution,grid=[8,9],pady=8,padx=12)
app.display()
