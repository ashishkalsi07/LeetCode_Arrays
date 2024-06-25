class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = 1 
        ans=[]
        for i in range(0,n):
            res = res * nums[i]
        print(res)
        for i in range(0,n):
            x = int(res / nums[i])
            ans.append(x)
        return ans
S=Solution()
nums=[-1,1,0,-3,3]
ans=S.productExceptSelf(nums)
print(ans)