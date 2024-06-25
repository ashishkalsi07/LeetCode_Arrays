class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False



S=Solution()
nums=[1,2,3,1]
ans=S.containsDuplicate(nums)
print(ans)