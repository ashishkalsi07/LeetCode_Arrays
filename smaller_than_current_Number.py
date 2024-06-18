class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        arr_ans=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if (j != i) and (nums[i] > nums[j]):
                    count += 1
                    print(nums[j])
            arr_ans.append(count)
        return arr_ans

Sol=Solution()
nums=[8,1,2,2,3]
ans=Sol.smallerNumbersThanCurrent(nums)
print(ans)