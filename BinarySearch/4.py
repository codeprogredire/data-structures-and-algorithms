'''
In an array, the numbers are stored such that they are in increasing order, and
then in decreasing order. Find the maximum element.
2,3,4,6,7,12,5,1 --> 12
'''


def findPeak(nums):
    if len(nums)==1:
        return nums[0]
    else:
        lo=0
        hi=len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            #Only one element is present in the array
            if lo==hi:
                return nums[lo]
            #Only two element in the array and first one is > than second one
            if hi==lo+1 and nums[lo]>nums[hi]:
                return nums[lo]
            #Only two element in the array and first one is < than second one            
            if hi==lo+1 and nums[lo]<nums[hi]:
                return nums[hi]
            elif nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return nums[mid]
            elif nums[mid]<nums[mid-1]:
                hi=mid-1
            else:
                lo=mid+1

while True:
    nums=list(map(int,input('Enter space separated integers : ').split()))
    print(findPeak(nums))
