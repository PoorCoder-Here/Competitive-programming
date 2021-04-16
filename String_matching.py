def string_match(org,mat):
    ind=[]
    a=mat[0]
    i=0
    while i<len(org):
        if org[i]==a:
            ind.append(i)
        i+=1
    print(ind)
    l=len(mat)
    for i in ind:
        end=i+l
        s=org[i:end]
        if s==mat:
            return 1,i
    return 2,0

original=input("Enter the original string:")
pat=input("Enter the sub pattern to match with original string:")
res,index=string_match(original,pat)
l=len(pat)
if res==1:
    print("String matched")
    print("Matched at index ",index+1," to ",index+l)
else:
    print("Cant find a match")
