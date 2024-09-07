from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf') # use the built-in float negative infinity to compare with the profit
        for i in range(len(prices)): # start of the buying point (buying index)
            for j in range(i+1, len(prices)): # selling index starting at i + 1
                profit = prices[j] - prices[i]
                if profit > 0:
                    max_profit = max(max_profit, profit)  # update max_profit if profit is greater
        return max_profit if max_profit > float('-inf') else 0 

# Test
def main() -> None:
    prices = [6,1,5,2,6,4]
    sol = Solution()
    print(sol.maxProfit(prices))

if __name__ == '__main__':
    main()