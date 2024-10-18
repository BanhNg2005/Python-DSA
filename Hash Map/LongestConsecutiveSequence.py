from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # counter = 0
        # res = defaultdict(int)
        #
        # for i in nums:
        #     if i not in res:
        #         left = res[i - 1] if i - 1 in res else 0
        #         right = res[i + 1] if i + 1 in res else 0
        #
        #         length = left + right + 1
        #         res[i] = length
        #         res[i - left] = length
        #         res[i + right] = length
        #         counter = max(counter, length)
        #
        # return counter

        s = set(nums) # create a set of the numbers in the list
        longest = 0 # initialize the longest variable to 0 to compare against
        for i in nums:
            if i - 1 not in s: # if the number before the current number is not in the set
                next_num = i + 1 # check the next number
                length = 1 # initialize the length to 1
                while next_num in s:
                    length += 1 # increment the length since it is consecutive
                    next_num += 1 # increment the next number to check
                longest = max(longest, length) # if the next_num no longer exists in the set, update the longest variable
        return longest

        # Time complexity: O(n)
        # Space complexity: O(n)

def main() -> None:
    nums1 = [100, 4, 200, 1, 3, 2]
    # expected: 4
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    # expected: 9
    nums3 = [1, 2, 3, 4]
    # expected: 4
    sol = Solution()
    print(sol.longestConsecutive(nums1))
    print(sol.longestConsecutive(nums2))
    print(sol.longestConsecutive(nums3))

if __name__ == '__main__':
    main()