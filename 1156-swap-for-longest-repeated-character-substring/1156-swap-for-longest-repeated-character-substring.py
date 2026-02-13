class Solution:
    def maxRepOpt1(self, text: str) -> int:
        if len(set(text))==1:
            return len(text)
        d={}
        for i in text:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=0
        for c in d:
            s = ""
            wrong = 0
            for ch in text:
                s += ch
                if ch != c:
                    wrong += 1
                while wrong > 1:
                    if s[0] != c:
                        wrong -= 1
                    s = s[1:]
                ans = max(ans, min(len(s), d[c]))
        return ans


        

        