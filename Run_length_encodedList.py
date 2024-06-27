class Solution(object):
    def decompressRLElist(self, nums):
        result=[]
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            result.extend([val] * freq)
        return result

S=Solution()
nums=[1,2,3,4]
ans=S.decompressRLElist(nums)
print(ans)