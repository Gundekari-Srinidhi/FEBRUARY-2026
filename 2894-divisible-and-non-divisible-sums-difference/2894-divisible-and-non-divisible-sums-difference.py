class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        divisible=0
        not_divisible=0
        for i in range(1,n+1):
            if i%m!=0:
                not_divisible+=i
            else:
                divisible+=i
        return not_divisible-divisible
        