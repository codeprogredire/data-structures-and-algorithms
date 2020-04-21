'''
Is x(an integer) a square?
i.e a*a=x for some integer a
'''

def checkSquare(x):
    if x==0 or x==1:
        return True
    else:
        nums=list(range(2,x+1))
        lo=0
        hi=x-1

        while lo<=hi:
            mid=(lo+hi)//2
            a=nums[mid]
            a*=a
            if a==x:
                return True
            elif a>x:
                hi=mid-1
            else:
                lo=mid+1
        return False

while True:
    print(checkSquare(int(input())))
