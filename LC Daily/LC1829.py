from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        result = []
        n = len(nums)
        mask = (1 << maximumBit) - 1 # create a mask to XOR with the elements in the list

        for i in range(n):
            mask = mask ^ nums[i] # XOR the mask with the current element
            result.append(mask) # append the result to the list

        return result[::-1] # reverse the list to get the correct order

    # Time complexity: O(n)
    # Space complexity: O(1)

def main() -> None:
    nums = [0,1,1,3]
    maximumBit = 2
    # expected: [0,3,2,3]
    nums1 = [2,3,4,7]
    maximumBit1 = 3
    # expected: [5,2,6,5]
    sol = Solution()
    print(sol.getMaximumXor(nums, maximumBit))
    print(sol.getMaximumXor(nums1, maximumBit1))

if __name__ == '__main__':
    main()