'''
Link : https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/
Question : Factorial
'''

from sys import stdin,stdout
MOD=10**9+7

table=[1,1]
for i in range(2,100001):
    value=(i*table[i-1])%MOD
    table.append(value)

for _ in range(int(stdin.readline())):
    N=int(stdin.readline())
    stdout.write(str(table[N])+'\n')


