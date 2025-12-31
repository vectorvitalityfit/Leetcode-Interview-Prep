"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing one day to buy and a later day to sell.
Return the maximum profit you can achieve. If no profit is possible, return 0.

Example 1:
Input: prices=[7,1,5,3,6,4]
Output: 5

Example 2:
Input: prices=[7,6,4,3,1]
Output: 0

Constraints:
1<=prices.length<=10^5
0<=prices[i]<=10^4
"""

class Solution(object):
    def maxProfit(self,prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum_price=float('inf')
        max_profit=0
        for price in prices:
            if price<minimum_price:
                minimum_price=price
            else:
                profit=price-minimum_price
                if profit>max_profit:
                    max_profit=profit
        return max_profit
    
    # Time Complexity: O(n), one pass through prices
    # Space Complexity: O(1), only two variables used