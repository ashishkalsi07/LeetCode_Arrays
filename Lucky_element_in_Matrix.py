import numpy as np
class Solution(object):
    def luckyNumbers (self, matrix):
        lucky_numbers = []
        matrix = np.array(matrix)

    # Iterate through each row to find the minimum element in the row
        for i in range(matrix.shape[0]):
            row_min = np.min(matrix[i, :])
            min_col_index = np.argmin(matrix[i, :])

            # Check if the row minimum is the maximum in its column
            if row_min == np.max(matrix[:, min_col_index]):
                lucky_numbers.append(row_min)

        return lucky_numbers

Sol=Solution()
nums=[[1,10,4,2],[9,3,8,7],[15,16,17,12]]
ans=Sol.luckyNumbers(nums)
print(ans)