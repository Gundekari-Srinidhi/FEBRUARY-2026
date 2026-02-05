class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):

        def solve(A, B):
            n = len(nums)

            # --- first A window ---
            l = 0
            r = A
            sumA = sum(nums[l:r])
            bestA = sumA

            # --- first B window ---
            l2 = r
            r2 = r + B
            sumB = sum(nums[l2:r2])

            ans = bestA + sumB

            # slide B window
            while r2 < n:
                # slide A window
                sumA += nums[r] - nums[l]
                l += 1
                r += 1
                bestA = max(bestA, sumA)
                sumB += nums[r2] - nums[l2]
                l2 += 1
                r2 += 1

                ans = max(ans, bestA + sumB)

            return ans

        return max(
            solve(firstLen, secondLen),
            solve(secondLen, firstLen)
        )
