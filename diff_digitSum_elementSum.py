class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elementSum=sum(nums)
        n=len(nums)
        digits = []
        for number in nums:
            for digit in str(number):
                digits.append(int(digit))
        ans=sum(digits)
        return elementSum - ans

S=Solution()
nums=[1,2,3,4]
ans=S.differenceOfSum(nums)
print(ans)        