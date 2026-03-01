class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n=len(s)
        words.sort()
        m=len(words)
        k=len(words[0])
        v=k*m
        ls=[]
        for i in range(0,n-k*m+1):
            sub=s[i:i+v]
            parts=[]
            for j in range(0,len(sub),k):
                parts.append(sub[j:j+k])
            if sorted(parts)==words:
                ls.append(i)
        return ls


        