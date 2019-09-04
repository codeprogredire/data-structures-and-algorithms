'''
Returns the single combinatiuon of four elements whose sum is equal to the specified target.
Time complexitiy: O(n2 logn)
'''

class PairSum:
    def __init__(self,first,second,sum):
        self.first=first
        self.second=second
        self.sum=sum

    def nocommon(self,obj):
        if self.first==obj.first or self.first==obj.first or self.second==obj.first or self.second==obj.second:
            return False
        
        return True



nums=[int(i) for i in input().split()]

n=len(nums)

target=int(input())

aux=[]

for i in range(n-1):
    for j in range(i+1,n):
        aux.append(PairSum(i,j,nums[i]+nums[j]))

aux.sort(key=lambda x: x.sum)

n=len(aux)

i=0
j=n-1

while i<j:
    if aux[i].sum+aux[j].sum==target and aux[i].nocommon(aux[j]):
        print(nums[aux[i].first],nums[aux[i].second],nums[aux[j].first],nums[aux[j].second])
        exit(0)
    elif aux[i].sum+aux[j].sum<target:
        i+=1
    else:
        j-=1

print('no such combination exists')