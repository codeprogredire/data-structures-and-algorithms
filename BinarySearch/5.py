'''
Greatest number less than x.
'''

import bisect

def search(nums,x):
    i=bisect.bisect_left(nums,x)
    if i:
        return i-1
    else:
        return -1

nums=list(map(int,input().split()))
target=int(input())

index=search(nums,target)
if index==-1:
    print('No number in list smaller than {}'.format(target))
else:
    print('Largest number smaller than {} is {}'.format(target,nums[index]))
