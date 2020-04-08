'''
Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.
Check whether A has redundant braces or not.
Return 1 if A has redundant braces, else return 0.
Note: A will be always a valid expression.

I/P: ((a+b)) O/P:1
I/P: ((a+b)+c) O/P:0
'''

class Solution:
    def braces(self, A):
        stack = []
        for i in A:
            if i is not ')':
                stack.append(i)
            else:
                if stack[-1]=='(':
                    return 1
                else:
                    item=0
                    ans=1
                    while item!='(':
                        item=stack.pop()
                        if item=='+' or item=='-' or item=='*' or item=='/':
                            ans=0
                    if item=='(' and ans==1:
                        return 1
        return 0

solution = Solution()
print(solution.braces('(a+b)'))
print(solution.braces('((a+b))'))
print(solution.braces('((a+b)+c)'))

