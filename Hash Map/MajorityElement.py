from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        for i in nums: # iterate through the list
            if i in counter: # if it is already in the counter, increment the count
                counter[i] += 1
            else: # if it is not in the counter, add it to the counter
                counter[i] = 1

        max_count = -1 # just a dummy value to compare against
        ans = -1 # same as above

        for key, val in counter.items(): # iterate through the counter
            if val > max_count:
                max_count = val # update the max_count
                ans = key # update the ans
        return ans # return the key with the highest frequency

        # Time complexity: O(n) since we iterate through the list and the counter
        # Space complexity: O(n) since we store the frequency of each element in the list


def main() -> None:
    nums = [3,2,3]
    # expected: 3
    nums1 = [2,2,1,1,1,2,2]
    # expected: 2
    sol = Solution()
    print(sol.majorityElement(nums))
    print(sol.majorityElement(nums1))

if __name__ == '__main__':
    main()