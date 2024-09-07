from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > 0:
                    max_profit = max(max_profit, profit)
        return max_profit if max_profit > float('-inf') else 0

def main() -> None:
    prices = [6,1,5,2,6,4]
    sol = Solution()
    print(sol.maxProfit(prices))

if __name__ == '__main__':
    main()