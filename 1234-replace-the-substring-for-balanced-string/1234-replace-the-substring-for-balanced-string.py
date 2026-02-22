class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        val = n // 4

        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        ok = True
        for c in "QWER":
            if c not in d or d[c] != val:
                ok = False
                break
        if ok:
            return 0

        left = 0
        ans = n

        for right in range(n):

            d[s[right]] -= 1

            while True:

                good = True
                for c in "QWER":
                    if c in d and d[c] > val:
                        good = False
                        break

                if not good:
                    break

                ans = min(ans, right - left + 1)
                d[s[left]] += 1
                left += 1

        return ans