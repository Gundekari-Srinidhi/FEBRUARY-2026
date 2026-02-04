class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        ans = 0

        for i in range(n1):
            # pruning: no need to try if remaining length is already smaller
            if n1 - i <= ans:
                break

            for j in range(n2):
                if n2 - j <= ans:
                    break

                k = 0
                while i + k < n1 and j + k < n2 and nums1[i + k] == nums2[j + k]:
                    k += 1

                ans = max(ans, k)

        return ans
