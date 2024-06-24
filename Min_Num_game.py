class Solution(object):
    def numberGame(self, nums):
        arr = []
        while nums:
            # Alice picks the smallest number
            alice = min(nums)
            nums.remove(alice)
            # If there are still numbers left, Bob picks the next smallest number
            if nums:
                bob = min(nums)
                nums.remove(bob)
                arr.append(bob)
                arr.append(alice)
        return arr

S=Solution()
nums=[2,7,9,6,4,6]  # this test case was getting failed , so I had to try with this
ans=S.numberGame(nums)
print(ans)