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

# Improved version
def isValid(s):
    stack=list()
    brackets={
        '}':'{',
        ']':'[',
        ')':'('
    }

    for i in range(len(s)):
        if s[i] not in brackets:
            stack.append(s[i])
        elif A[i] in brackets:
            if len(stack)==0 or brackets[s[i]]!=stack.pop():
                return 'NO'
    if len(stack)==0:
        return 'YES'
    else:
        return 'NO'

print(isValid('['))