class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i > j and nums[i] == nums[j]:
                    count += 1
        return count





Sol=Solution()
nums=[1,1,1,1]
ans=Sol.numIdenticalPairs(nums)
print(ans)        