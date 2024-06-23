class Solution(object):
    def runningSum(self, nums):
        l=[]
        n=0
        for i in nums:
            n += i
            l.append(n)
        return l

S=Solution()
nums=[3,1,2,10,1]
ans=S.runningSum(nums)
print(ans)