class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxcandy=max(candies)
        ans=[]
        for i in candies:
            if i + extraCandies >= maxcandy:
                ans.append(True)
            else:
                ans.append(False)
        return ans



Sol=Solution()
candies=[2,3,5,1,3]
extracandies=3
ans=Sol.kidsWithCandies(candies,extracandies)
print(ans)

