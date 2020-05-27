'''
Link: https://leetcode.com/problems/minimum-path-sum/
'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        a=[[0]*n]*m
        
        for i in range(m):
            for j in range(n):
                if i==0:
                    if j==0:
                        a[i][j]=grid[i][j]
                    else:
                        a[i][j]=a[i][j-1]+grid[i][j]
                elif j==0:
                    a[i][j]=a[i-1][j]+grid[i][j]
                else:
                    a[i][j]=min(a[i-1][j],a[i][j-1])+grid[i][j]
                    
        
        return a[m-1][n-1]
        