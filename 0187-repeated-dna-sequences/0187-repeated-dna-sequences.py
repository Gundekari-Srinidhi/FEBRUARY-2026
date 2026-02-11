class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<=10:
            return []
        d={}
        l=0
        r=10
        ls=[]
        while r<=len(s):
            val=s[l:r]
            if val in d:
                d[val]+=1
                ls.append(val)
            else:
                d[val]=1
            r+=1
            l+=1
        return list(set(ls))
                

        