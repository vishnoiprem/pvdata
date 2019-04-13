# Time:  O(n)
# Space: O(1)
#
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in A:

            local_max, local_min = max(x, local_max * x, local_min * x), min(x, local_max * x, local_min * x)

            global_max = max(global_max, local_max)
            print('local_max-',local_max,'local_min-',local_min,'global_max-',global_max)

        return global_max



if __name__ == "__main__":
    print (Solution().maxProduct([2, 3, -2, 4]))
    print (Solution().maxProduct([-4,-3]))