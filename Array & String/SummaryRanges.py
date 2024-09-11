from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i] # start of the range

            # the loop checks to make sure the loop doesn't go out of bounds 
            # and that the next element is one greater than the current element
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            if start != nums[i]:
                ans.append(f"{start}->{nums[i]}") # if the range is greater than 1, append the range
            else:
                ans.append(str(nums[i]))
            i += 1

        return ans
        # Time complexity: O(n) because even though we have a nested while loop, 
        # the inner while loop will only run once for each element in the list from the first while loop
        # Space complexity: O(1) since we are not using any extra space

def main() -> None:
    nums = [0, 1, 2, 4, 5, 7]
    sol = Solution()
    print(sol.summaryRanges(nums))

if __name__ == '__main__':
    main()           