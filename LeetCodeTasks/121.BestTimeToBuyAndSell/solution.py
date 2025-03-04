'''
class Solution:
    from typing import List
    def maxProfit(self, prices: List[int]) -> int:
        mp, minEl = 0, min(prices)
        for i in range(prices.index(minEl), len(prices)):
            res = prices[i] - minEl
            mp = res if mp < res else mp
        return mp
'''

class Solution:
    from typing import List
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        mnprice, mxprof = prices[0], 0
        for price in prices:
            if price < mnprice:
                mnprice = price
            else:
                mxprof = max(mxprof, price - mnprice)
        return mxprof


def main():
    solution = Solution()
    print(solution.maxProfit(prices=[7,1,5,3,6,4]))
    print(solution.maxProfit(prices=[7,6,4,3,1]))
    print(solution.maxProfit(prices=[2,4,1]))
    print(solution.maxProfit(prices=[1,2]))

if __name__ == '__main__':
    main()
