'''
Link : https://leetcode.com/problems/climbing-stairs
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        else:
            table=[1,1]
            for i in range(2,n+1):
                temp=table[i-1]+table[i-2]
                table.append(temp)
        
            return table[n]
