class Solution:
    def queryString(self, s: str, n: int) -> bool:
        def binary(n):
            res=""
            if n==0:
                print(0)
            else:
                while(n!=0):
                    rem=n%2
                    res+=str(rem)
                    n=n//2
            return res[::-1]
        for i in range(1,n+1):
            if binary(i) not in s:
                return False
        return True
                