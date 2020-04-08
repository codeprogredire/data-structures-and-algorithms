'''
Reverse a string using Stack.
'''

string = input('Enter a string : ')
stack = list(string)
rev = ''

while stack:
    rev+=stack.pop()

print('Original string : {}'.format(string))
print('Reversed string : {}'.format(rev))
