class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        zero=True
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if i==j or j==(n-i-1):
                    if grid[i][j]==0:
                        zero=False
                else:
                    if grid[i][j]!=0:
                        zero=False
        return zero
        
        