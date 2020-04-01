'''
Balanced Brackets
Link : https://www.hackerrank.com/challenges/balanced-brackets/problem
'''

def isBalanced(s):
    stack=[]
    for i in s:
        if i in '({[':
            stack.append(i)
        else:
            if (len(stack)==0) or (i==')' and stack[-1]!='(') or (i=='}' and stack[-1]!='{') or (i==']' and stack[-1]!='['):
                return 'NO'
            else:
                del(stack[-1])
            
    if len(stack)==0:
        return 'YES'
    else:
        return 'NO'

print(isBalanced('{}[]'))