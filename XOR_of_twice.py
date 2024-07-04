from functools import reduce
from operator import ixor
class Solution(object):
    def duplicateNumbersXOR(self, nums):
        fre={}
        for i in nums:
            if i in fre:
                fre[i] += 1
            else:
                fre[i] = 1
        ans=[]
        for i in fre:
            if fre[i] == 2:
                ans.append(i)
        if len(ans) == 0:
            return 0
        res = reduce(ixor,ans)
        if res:
            return(res)
        else:
            return 0
S=Solution()
nums=[1,2,3]
S.duplicateNumbersXOR(nums)
