class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        n=len(nums)
        a = nums[0] * nums[1]
        b = nums[n-1] * nums[n-2]
        return b-a 


S=Solution()
nums=[4,2,5,9,7,4,8]
ans=S.maxProductDifference(nums)
print(ans)