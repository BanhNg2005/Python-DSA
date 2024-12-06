from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        result = 0 # return the number of time we make an addition
        current_sum = 0
        banned = set(banned) # we make banned a set to search for the number in O(1) time
        for i in range(1, n+1): # we want to count from 1 up to n
            if current_sum >= maxSum or current_sum + i > maxSum:
                break
            elif i not in banned:
                current_sum += i
                result += 1
        return result

        # TIme: O(n)
        # Space: O(n)

        # Another way but different if condition
        # current_sum = 0
        # result = 0
        # banned = set(banned)
        # for i in range(1, n+1):
        #     if i not in banned and current_sum + i <= maxSum:
        #         current_sum += i
        #         result += 1
        # return result

def main() -> None:
    banned = [1,6,5]
    n = 5
    maxSum = 6
    # expected: 2
    banned1 = [1,2,3,4,5,6,7]
    n1 = 8
    maxSum1 = 1
    # expected: 0
    sol = Solution()
    print(sol.maxCount(banned, n, maxSum))
    print(sol.maxCount(banned1, n1, maxSum1))

if __name__ == '__main__':
    main()
