class Solution(object):
    def moveZeroes(self, nums):
        for i in nums:
            if i == 0:
                nums.append(i)
                nums.remove(i)
        print(nums)


S=Solution()
nums=[0]
S.moveZeroes(nums)