class Solution(object):
    def maximizeSum(self, nums, k):
        nums.sort()
        sum = 0
        while(k > 0):
            x = max(nums)
            sum = sum + x
            nums.remove(x)
            y = x + 1
            nums.append(y)
            k=k-1
        print(sum)



S=Solution()
nums=[5,5,5]
k=2
ans=S.maximizeSum(nums,k)
