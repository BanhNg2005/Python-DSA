from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]

        max_avg = curr_sum / k

        for i in range(k, n):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]

            avg = curr_sum / k
            max_avg = max(max_avg, avg)

        return max_avg

    # Time complexity: O(n)
    # Space complexity: O(1)

def main() -> None:
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    # expected: 12.75
    nums1 = [5]
    k1 = 1
    # expected: 5.0
    sol = Solution()
    print(sol.findMaxAverage(nums, k))
    print(sol.findMaxAverage(nums1, k1))

if __name__ == '__main__':
    main()