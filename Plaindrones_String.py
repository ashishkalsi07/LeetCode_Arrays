class Solution(object):
    def firstPalindrome(self, words):
        def is_palindrome(s):
            return s == s[::-1]

        for word in words:
            if is_palindrome(word):
                return word
        return ""
        

S=Solution()
nums=["abc","def","ada"]
ans=S.firstPalindrome(nums)
print(ans)