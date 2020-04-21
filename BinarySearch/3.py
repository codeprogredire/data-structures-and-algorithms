'''
(Lower Bound Problem)
Given a sorted array, find the first number >= x.
'''

def check(nums,target):
    if len(nums)==1:
        if nums[0]>=target:
            return nums[0]
        else:
            return -1
    else:
        lo=0
        hi=len(nums)-1
        ans=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return nums[mid]
            elif nums[mid]>target:
                ans=nums[mid]
                hi=mid-1
            else:
                lo=mid+1
    
    return ans

while check:
    nums=list(map(int,input('Enter space separated integers : ').split()))
    target=int(input('Enter x : '))
    print(check(nums,target))