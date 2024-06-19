import numpy as np
class Solution(object):
    def luckyNumbers (self, matrix):
        lucky_numbers = []
        matrix = np.array(matrix)

   
        for i in range(matrix.shape[0]):
            row_min = np.min(matrix[i, :])
            min_col_index = np.argmin(matrix[i, :])

            
            if row_min == np.max(matrix[:, min_col_index]):
                lucky_numbers.append(row_min)

        return lucky_numbers

Sol=Solution()
nums=[[1,10,4,2],[9,3,8,7],[15,16,17,12]]
ans=Sol.luckyNumbers(nums)
print(ans)