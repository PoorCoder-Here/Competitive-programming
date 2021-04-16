def insert(intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        temp=list(intervals)
        i=0
        while i<len(temp)-1:
            if temp[i][1]>=temp[i+1][0]:
                j=i
                l=i+1
                while l<len(temp) and temp[j][1]>=temp[l][0]:
                    if temp[j][1]<temp[l][1]:
                        temp[j][1]=temp[l][1]
                    l+=1
                i=l
            else:
                i+=1
        k=0
        inc=0
        while k<len(temp)-1:
            if temp[k][1]>=temp[k+1][0]:
                w=k
                h=k+1
                try:
                    while temp[w][1]>=temp[h][0]:
                        temp.pop(h)
                    break
                except:
                    break
            else:
                k+=1
        return(temp)
print(insert([[1,3],[6,9]],[2,5]))
