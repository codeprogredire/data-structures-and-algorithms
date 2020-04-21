'''
In an array, the numbers are stored such that they are in increasing order, and
then in decreasing order. Find the maximum element.
'''


def findPeak(nums):
    if len(nums)==1:
        return nums[0]
    elif len(nums)==2:
        return max(nums)
    else:
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if lo==hi:
                return nums[mid]
            elif nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return nums[mid]
            elif nums[mid]<nums[mid-1]:
                hi=mid-1
            else:
                lo=mid+1

while True:
    nums=list(map(int,input('Enter space separated integers : ').split()))
    print(findPeak(nums))
