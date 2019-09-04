'''
    Kadane's algorithm is used to find the largest sum possible selecting a contiguous sub-array from the given array.
    The time complexity of the algorithm is : O(n)
'''


print('Enter space-separated integers : ')

nums=[int(i) for i in input().split()]

max_so_far = max_ending_here = 0

for number in  nums:
    max_ending_here += number
    if max_ending_here < 0:
        max_ending_here = 0
    if max_so_far < max_ending_here:
        max_so_far = max_ending_here

print('The largest sum possible selecting a contiuguos sub-array from the given array is : ',max_so_far)