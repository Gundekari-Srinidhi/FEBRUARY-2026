class Solution:
    def triangleType(self, nums: List[int]) -> str:
        l=len(set(nums))
        a,b,c=nums
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"
        if l==1:
            return "equilateral"
        elif l==2:
            return "isosceles"
        else:
            return  "scalene" 
        