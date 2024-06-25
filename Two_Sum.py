class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return i,j
      
S=Solution()
nums=[2,3,4]
target=7
ans=S.twoSum(nums,target)
print(ans)