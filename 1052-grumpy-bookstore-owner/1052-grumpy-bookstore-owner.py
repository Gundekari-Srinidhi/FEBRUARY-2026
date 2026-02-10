class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        max1=0
        for i in range(n):
            if grumpy[i]==0:
                max1+=customers[i]
        sum1=0
        for i in range(minutes):
            if grumpy[i]==1:
                sum1+=customers[i]
        max1+=sum1
        l=0
        r=minutes-1
        sum1=max1
        while r<n-1:
            if grumpy[l]==1:
                sum1-=customers[l]
            if grumpy[r+1]==1:
                sum1+=customers[r+1]
            l+=1
            r+=1
            max1=max(max1,sum1)
        return max1
            
            

        