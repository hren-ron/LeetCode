'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        if(not prices):
            return(0)
        lenght=len(prices)
        profit=0
        i=0
        while(i<lenght-1):
            
            while(i<lenght-1 and prices[i]>=prices[i+1]):
                i=i+1
            lower=prices[i]
            while(i<lenght-1 and prices[i]<=prices[i+1]):
                i=i+1
            high=prices[i]
            profit=profit+high-lower
        return(profit)
        '''
        profit=0
        for i in range(1,len(prices)):
            if(prices[i]>prices[i-1]):
                profit+=prices[i]-prices[i-1]
        return(profit)
        