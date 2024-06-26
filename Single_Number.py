'''To find the element that appears only once in a list where every other element appears twice, you can use the XOR bitwise operator. XOR has the property that 𝑎 ⊕ 𝑎 = 0 a⊕a=0 and  𝑎 ⊕ 0 = 𝑎 a⊕0=a. Thus, if you XOR all the elements in the list together, the duplicate elements will cancel out, leaving only the element that appears once.'''

'''another approach to find the element that appears only once in a list where every other element appears twice is to use a hash table (dictionary)'''

class Solution(object):
    def singleNumber(self, nums):
        # result = 0
        # for num in nums:
        #     result ^= num
        # return result 
        fre={}
        an=[]
        for i in nums:
            if i in fre:
                fre[i] += 1
            else:
                fre[i] = 1
        for i in fre:
            if fre[i] == 1:
                an.append(i)
        return an

        
S=Solution()
nums=[1,2,3,1,2,4,5,4,5,4,7]
ans=S.singleNumber(nums)
print(ans)