class Solution:
    def maxSlidingWindow(self, nums, k):

        n = len(nums)
        if n == k:
            return [max(nums)]

        l = 0
        r = 0
        dq = []
        ans = []

        while r < n:

            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            if dq[0] < l:
                dq.pop(0)

            if r - l + 1 == k:
                ans.append(nums[dq[0]])
                l += 1

            r += 1

        return ans