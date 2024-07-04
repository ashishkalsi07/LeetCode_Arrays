class Solution(object):
    def addedInteger(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        x = nums2[0] - nums1[0]
        return x




S=Solution()
nums1=[1,1,1,1]
nums2=[1,1,1,1]
ans=S.addedInteger(nums1,nums2)
print(ans)