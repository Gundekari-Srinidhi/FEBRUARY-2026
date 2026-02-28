class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s1=0
        for n in nums:
            count = 0
            s=0
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    j=n//i
                    if i == j:
                        count += 1
                        s+=i
                    else:
                        count += 2
                        s+=i+j
                if count > 4:
                    break
            if count==4:
                s1+=s
        return s1
        