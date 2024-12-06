from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1 # set to 1 since the first element in the array is always unique and doesn't need to be changed
        for i in range(1, len(nums)): # starts from 1 because we need to compare each element with its prev element
            if nums[i] != nums[i - 1]: # if not equal means we have encountered a new unique element
                nums[j] = nums[i] # update nums[j] with te value of the unique element at nums[i]
                j += 1 # increment to next position for a unique element
        return j # j represents the length of the resulting array with duplicates removed

def main() -> None:
    nums1 = [1, 1, 2]
    # expected: 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # expected: 5
    sol = Solution()
    print(sol.removeDuplicates(nums1))
    print(sol.removeDuplicates(nums2))

if __name__ == '__main__':
    main()