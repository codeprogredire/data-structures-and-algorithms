'''
Link : https://www.codechef.com/LRNDSA04/problems/STACKS
'''


from sys import stdin,stdout

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    disks=[int(i) for i in stdin.readline().split()]

    stack=[]
    for rad in disks:
        if len(stack)==0:
            stack.append(rad)
        else:
            lo=0
            hi=len(stack)-1
            index=-1
            while lo<=hi:
                mid=(lo+hi)//2
                if stack[mid]>rad:
                    index=mid
                    hi=mid-1
                else:
                    lo=mid+1
            
            if index==-1:
                stack.append(rad)
            else:
                stack[index]=rad
                
    
    stdout.write(str(len(stack))+' ')
    for rad in stack:
        stdout.write(str(rad)+' ')
    stdout.write('\n')

