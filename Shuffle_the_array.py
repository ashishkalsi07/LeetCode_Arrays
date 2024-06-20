class Solution(object):
    def shuffle(self, nums, n):
        result=[]
        for i in range(n):
            x=n
            result.append(nums[i])
            result.append(nums[x+i])
        return result
             
  
Sol=Solution()
n=3
nums=[2,5,1,3,4,7]
ans=Sol.shuffle(nums,n)
print(ans)
