class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum=0 
        digit_sum=0
        for val in nums:
            element_sum+=val
            while val>0:
                rem=val%10
                digit_sum+=rem
                val=val//10
        return abs(element_sum-digit_sum)

        