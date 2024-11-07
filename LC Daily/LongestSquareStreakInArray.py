from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = sorted(set(nums)) # sort the list and remove duplicates by converting it to a set
        nums_set = set(nums) # we want to store the elements in the list in a set for faster lookup
        max_strk = 0

        for n in nums:
            strk = 0
            while n in nums_set:
                strk += 1
                n = n * n
            if strk > 1:
                max_strk = max(max_strk, strk)
        return max_strk if max_strk > 1 else -1

def main() -> None:
    nums = [2,3,5,6,7]
    # expected: -1
    nums1 = [4,3,6,16,8,2]
    # expected: 3
    sol = Solution()
    print(sol.longestSquareStreak(nums))
    print(sol.longestSquareStreak(nums1))

if __name__ == '__main__':
    main()