class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res=[''] * len(indices)
        for i , index in enumerate(indices):
            res[index]=s[i]
        ans=''.join(res)
        return ans

S=Solution()
str="abc"
indices=[0,1,2]
ans=S.restoreString(str,indices)
print(ans)