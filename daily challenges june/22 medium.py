"""
You are given an array prices where prices[i] is the price of a given stock on the ith day, 
and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like,
 but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""


# class Solution:
def maxProfit(prices: list[int], fee: int) -> int:
    # cash = 0
    # hold = -prices[0]  # Assuming we buy the stock on the first day

    # for i in range(1, len(prices)):
    #     prevCash = cash
    #     prevHold = hold

    #     cash = max(prevCash, prevHold + prices[i] - fee)
    #     hold = max(prevHold, prevCash - prices[i])
    # print(cash)
    # return cash
    buy = float('-inf')
    sell = 0

    for price in prices:
        buy = max(buy, sell - price)
        sell = max(sell, buy + price - fee)
    return sell
maxProfit([100,122,1,2,3,1,4,1,41,2,100], 100)