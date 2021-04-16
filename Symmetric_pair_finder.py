l=[(1,3),(2,6),(3,5),(7,4),(5,3),(8,7)]
dict={}
for i in l:
    j=i
    dict[j[0]]=j[1]
li=[]
for key,value in dict.items():
    find=value
    test=key
    try:
        ans=dict[find]
        if ans==test:
            li.append((find,test))
            li.append((test,find))
    except:
        continue
print(list(set(li)))
            
