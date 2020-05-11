from sys import stdin,stdout
import bisect

n=int(stdin.readline())

nums=list(map(int,stdin.readline().split()))

temp=[]
tot=0
for i in range(n):
    j=bisect.bisect(temp,nums[i])
    tot+=(i-j)
    temp.insert(j,nums[i])

stdout.write(str(tot))




    