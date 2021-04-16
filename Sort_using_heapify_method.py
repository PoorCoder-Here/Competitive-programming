#Sorting the elements based on heapify method using percolate up method
import numpy as np
import datetime as dt
s=[9,1,3,10,2,6,8,1,4,12,34,14,56,87,90,12,65,76,89,23,54,76,40,90,78,98,20,80,30,190]
print(dt.datetime.now())
#s1=np.random.permutation(100)#To create a np object of random numbers from 0 to 99
s1=list(s)#To convert the np object to list
print("Elements before sorting:",s1)
"""
Heapify method to traverse in left child and right child
def left_o_left(s,i):
    if (2*i+1)<len(s)-1 and s[i]>s[2*i+1]:
        return 2*i+1
    else:
        j=2*i+1
        ind=j
        while j>0:
            j=int((i-1)/2)
            if s[j]<s[2*j+1]:
                s[j],s[j*2+1]=s[j*2+1],s[j]
                i=j
            else:
                return ind
    return len(s)
def right_o_right(s,i):
    if (2*i+2)<len(s)-1 and s[i]>s[2*i+2]:
        return 2*i+2
    else:
        j=2*i+2
        ind=j
        while j>0:
            j=int((i-1)/2)
            if s[j]<s[2*j+2]:
                s[j],s[2*j+2]=s[2*j+2],s[j]
                i=j
            else:
                return ind
    return len(s)
"""

def backtrace(s1,i): #Function to do percolate sorting from bottom to top (percolate up)
    j=int((i-1)/2)
    while j>=0 and s1[i]>s1[j]:
        s1[i],s1[j]=s1[j],s1[i]
        i=j
        j=int((i-1)/2)
i=len(s1)-1
j=len(s1)
sor_arr=[]
while j>0:
    while i>0:
        backtrace(s1,i)
        i-=1
    sor_arr.append(s1.pop(0))
    i=len(s1)-1
    j=len(s1)
"""i=0
while i<len(s):
    a=right_o_right(s,i)
    print("a:",a)
    i=a
"""
print(dt.datetime.now())
print("Elements after sorting:",sor_arr)
        
