from typing import List

class Solution():
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0] # the first number is the closest
        for x in nums:
            if abs(x) < abs(closest):
                closest = x # found the new closest number

        if closest < 0 and abs(closest) in nums: 
            return abs(closest) # return the positive number and not the negative
        else:
            return closest
        # Time: O(2n) or just O(n)
        # Space: O(1)

# Test case
def main() -> None:
    nums = [-2, -1, 1]
    sol = Solution()
    print(sol.findClosestNumber(nums))

if __name__ == '__main__':
    main()