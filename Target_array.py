class Solution(object):
    def createTargetArray(self, nums, index):
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target



S=Solution()
nums=[1,2,3,4]
index=[0,1,2,0]
ans=S.createTargetArray(nums,index)
print(ans)