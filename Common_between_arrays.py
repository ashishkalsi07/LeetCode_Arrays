class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        ans=[]
        count  = 0
        for i in nums1:
            if i in nums2:
                count = count + 1
        ans.append(count)
        count = 0
        for i in nums2:
            if i in nums1:
                count = count + 1
        ans.append(count)
        print(ans)

S=Solution()
nums1=[3,4,2,3]
nums2=[1,5]
ans=S.findIntersectionValues(nums1,nums2)