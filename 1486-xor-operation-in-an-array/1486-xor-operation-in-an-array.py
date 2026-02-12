class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        s=start
        val=start
        for i in range(n-1):
            val=val+2
            s=s^val
        return s
        