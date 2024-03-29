class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for i in xrange(0, 2)]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in xrange(2, len(nums)):
            dp[i%2] = max(dp[(i - 1)%2], dp[(i - 2)%2] + nums[i])
        return dp[(len(nums) - 1)%2]


# Time:  O(n)
# Space: O(1)
#
# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you 
# from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, 
# determine the maximum amount of money you can rob tonight without alerting the police.
#
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0
            
        if len(num) == 1:
            return num[0]
        
        num_i, num_i_1 = max(num[1], num[0]), num[0]
        for i in range(2, len(num)):
            num_i_1, num_i_2 = num_i, num_i_1
            num_i = max(num[i] + num_i_2, num_i_1);
        
        return num_i

    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now

    def rob3(self,nums):

        a=0
        b=0
        for i in range(len(nums)):

            if i%2==1:

                a=max(a+nums[i],b)
                
            else:
                b=max(b+nums[i],a)
        return max(a,b)



if __name__ == '__main__':
        print (Solution().rob3([8,4,8,5,9,6,5,4,4,10]))


