'''
Returns a single combination of four elements whose sum is equal to the target value specified.
Time complexity : O(n3)
'''

nums=[int(i) for i in input().split()]

target=int(input())

nums.sort()

n=len(nums)

for i in range(n-3):
    for j in range(i+1,n-2):
        k=j+1
        l=n-1
        while k<l:
            sum=nums[i]+nums[j]+nums[k]+nums[l]
            if sum==target:
                print(nums[i],nums[j],nums[k],nums[l])
                break
            elif sum<target:
                k+=1
            else:
                l-=1

