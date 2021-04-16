class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        dict1={}
        if strs==["",""]:
            return [["",""]]
        else:
            for i in strs:
                a=list(i)
                a.sort()
                if i not in dict:
                    dict[i]=[a.copy()]
                else:
                    temp=dict[i]
                    temp.append(a.copy())
                    dict[i]=temp.copy()
            for key,value in dict.items():
                #s="".join(value)
                h=0
                l=len(value)
                value1=value
                while h<l:
                    s="".join(value1[h])
                    if s not in dict1:
                        dict1[s]=[key]
                    else:
                        temp=dict1[s]
                        temp.append(key)
                        dict1[s]=temp.copy()
                        temp.clear()
                    h+=1
            fin=[]
            for key,value in dict1.items():
                fin.append(value)
            return fin
        
