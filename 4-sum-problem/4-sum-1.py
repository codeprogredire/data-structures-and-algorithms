'''
    Returns all the four elements combinations whose sum is equal to the target value specified. The combinations are
    separated by '$' delimiter. Time complexity : O(n4)
'''

t=int(input())

while t>0:
    
    n,target=[int(i) for i in input().split()]

    nums=[int(i) for i in input().split()]

    length = len(nums)

    nums.sort()

    quads=[]

    for i in range(length-3):
        for j in range(i+1,length-2):
            for k in range(j+1,length-1):
                for l in range(k+1,length):

                    if nums[i]+nums[j]+nums[k]+nums[l] == target:
                        temp=[nums[i],nums[j],nums[k],nums[l]]
                        quads.append(temp)

    
    
    if len(quads)==0:
        print(-1)
    else:
        for quad in quads:
            for i in quad:
                print(i,end=' ')
            print('$',end='')
                    
    print()
    t-=1
                    

