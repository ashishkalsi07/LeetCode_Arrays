class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        new_word1=''.join(word1)
        new_word2=''.join(word2)

        return new_word1 == new_word2


S=Solution()
word1=["ab","c"]
word2=["a","bcd"]
value=S.arrayStringsAreEqual(word1,word2)
print(value)