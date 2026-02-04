class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum=0 
        for val in nums:
            element_sum+=val
        digit_sum=0
        for val in nums:
            if val<=9:
                digit_sum+=val
            else:
                temp=val
                while temp>0:
                    rem=temp%10
                    digit_sum+=rem
                    temp=temp//10
        return abs(element_sum-digit_sum)

        