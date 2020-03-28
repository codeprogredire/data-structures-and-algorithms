'''
Generate all binary strings with n bits. Assume A[0,n-1] is an array of size n.
'''

def append_to_front_beginning(x,L):
    return [x + element for element in L]

def bit_strings(n):
    if n==0:
        return []
    if n==1:
        return ['0','1']
    else:
        return (append_to_front_beginning('0',bit_strings(n-1)) + append_to_front_beginning('1',bit_strings(n-1)))

print(bit_strings(3))