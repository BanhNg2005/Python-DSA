from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # easy solution using sort method
        # nums = [x ** 2 for x in nums]
        # nums.sort()
        # return nums

        # two pointer approach
        left = 0
        right = len(nums) - 1
        res = []

        while left <= right: # we need to include the equal sign to account for the case where left and right are the same
            if abs(nums[left]) > abs(nums[right]): # instead of squaring the numbers, we can just compare the absolute values
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1
        return res[::-1] # step backwards to reverse the list

        # or
        # res.reverse()
        # return res

        # Time complexity: O(n) because we have to go through from the left to the right of the list
        # Space complexity: O(1) as we don't assume any extra space because the solution requires the output array to be returned

def main() -> None:
    nums = [-4,-1,0,3,10]
    # expected: [0,1,9,16,100]
    nums1 = [-7,-3,2,3,11]
    # expected: [4,9,9,49,121]
    sol = Solution()
    print(sol.sortedSquares(nums))
    print(sol.sortedSquares(nums1))

if __name__ == '__main__':
    main()
