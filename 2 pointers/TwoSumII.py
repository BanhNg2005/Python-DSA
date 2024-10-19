from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1

        while l < r:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l+1, r+1] # the problem is 1-indexed
            elif summ > target: # the solution is sorted, so if the sum is greater than the target, we need to decrease the sum by moving the right pointer to the left
                r -= 1
            else: # if the sum is less than the target, we need to increase the sum by moving the left pointer to the right
                l += 1

        # Time complexity: O(n) because we are just moving the pointers left or right once
        # Space complexity: O(1) since we just have one variable summ to store the sum of the two numbers
def main() -> None:
    numbers = [2,7,11,15]
    target = 9
    # expected: [1,2]
    numbers1 = [2,3,4]
    target1 = 6
    # expected: [1,3]
    sol = Solution()
    print(sol.twoSum(numbers, target))
    print(sol.twoSum(numbers1, target1))

if __name__ == '__main__':
    main()