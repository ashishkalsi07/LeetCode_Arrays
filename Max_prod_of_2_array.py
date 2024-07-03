class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        a = (nums[n-1]-1) * (nums [n - 2]-1)
        return a 


S=Solution()
nums=[3,7]
ans=S.maxProduct(nums)
