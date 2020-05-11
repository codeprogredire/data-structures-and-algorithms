'''
Fibonacci number using Memoization
'''

def fib(n):
    table=[1,1]
    for i in range(2,n+1):
        value=table[i-1]+table[i-2]
        table.append(value)
    
    return table[n]

print(fib(4))
print(fib(2))

