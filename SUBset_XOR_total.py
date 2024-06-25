class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def generate_subsets(nums):
            # Function to generate all subsets
            subsets = [[]]
            for num in nums:
                subsets += [curr + [num] for curr in subsets]
            return subsets
        
        def xor_of_subset(subset):
            # Function to calculate the XOR of elements in a subset
            xor_result = 0
            for num in subset:
                xor_result ^= num
            return xor_result
        
        subsets = generate_subsets(nums)
        total_xor_sum = sum(xor_of_subset(subset) for subset in subsets)
        
        return total_xor_sum

S=Solution()
nums=[5,1,6]
ans=S.subsetXORSum(nums)
print(ans)