class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        ans=0
        min_pric=prices[0]




        for i in range(1,len(prices)):

            min_pric=min(min_pric,prices[i])

            ans=max(ans,prices[i]-min_pric)

        return ans




if __name__=="__main__":

    a=[7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(a))