class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1={}
        temp=""
        mapp=set()
        if len(s)!=len(t):
            return False
        else:
            for i in range(0,len(s)):
                if s[i] in dict1:
                    temp+=dict1[s[i]]
                else:
                    if t[i] in mapp:
                        return False
                    
                    dict1[s[i]]=t[i]
                    mapp.add(t[i])
                    temp+=t[i]
        return temp==t