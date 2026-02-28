class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):

        if valueDiff < 0:
            return False

        zero = False
        d = {}
        size = valueDiff + 1

        i = 0
        n = len(nums)

        while i < n:

            b = nums[i] // size

            if b in d:
                zero = True
                break

            if (b - 1) in d and abs(nums[i] - d[b - 1]) <= valueDiff:
                zero = True
                break

            if (b + 1) in d and abs(nums[i] - d[b + 1]) <= valueDiff:
                zero = True
                break

            d[b] = nums[i]

            if i >= indexDiff:
                old = nums[i - indexDiff] // size
                del d[old]

            i += 1

        return zero