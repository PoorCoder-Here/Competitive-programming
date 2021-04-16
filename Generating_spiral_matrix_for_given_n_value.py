def generateMatrix(n):
        i=0
        j=0
        matrix=[]
        while i<n:
            temp=[]
            while j<n:
                temp.append(0)
                j+=1
            matrix.append(temp)
            j=0
            i+=1
        up=0
        down=n-1
        left=0
        right=n-1
        i=1
        c=0
        while i<=n*n:
            while c<=right and i<=n*n:
                matrix[up][c]=i
                #print(matrix)
                i+=1
                c+=1
                #print("in up")
            up+=1
            c=up
            while c<=down and i<=n*n:
                matrix[c][right]=i
                #print(matrix)
                c+=1
                i+=1
                #print("in right")
            right-=1
            c=right
            while c>=left and i<=n*n:
                matrix[down][c]=i
                #print(matrix)
                i+=1
                c-=1
                #print("in down")
            down-=1
            c=down
            while c>=up and i<=n*n:
                matrix[c][left]=i
                #print(matrix)
                i+=1
                c-=1
                #print("in left")
            left+=1
            c=left
        return matrix

print(generateMatrix(20))
