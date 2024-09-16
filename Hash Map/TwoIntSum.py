from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # hashmap contains value : index
        # every element come before the current element will be checked in the hashmap
        # or every previous element will be stored in the hashmap

        for i, n in enumerate(nums): # iterate through every index, number in the array, 
            # enumerate method generates pairs of (index, value) for each element in the nums
            # ex: (0, 4), (1, 9), (2, 5), (3, 7)
            diff = target - n # calculate the difference between the target and the current number
            if diff in prevMap: # check if this difference is already in the hashmap
                return [prevMap[diff], i] # return the pair of indices, the index of the difference and the current index
            prevMap[n] = i # update the hashmap with the current number and its index

            # Time complexity: O(n) because we iterate through the array once 
            # and adding each value to the hashmap which is a constant time operation (O(1))
            # and checking if a value exists in the hashmap is also a constant time operation (O(1))
            # Space complexity: O(n) because we store n elements in the hashmap 
            # and could potentially add each value to the hashmap

def main() -> None:
    nums = [4, 9, 5, 7]
    target = 14
    sol = Solution()
    print(sol.twoSum(nums, target))

if __name__ == '__main__':
    main()