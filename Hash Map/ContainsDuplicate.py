from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Hash table approach
        # dup_dict = {} # number : frequency
        #
        # for i in nums:
        #     if i in dup_dict: # as it iterates through the list, if the number is found again, we can return true
        #         return True
        #     else:
        #         dup_dict[i] = 1 # if the number is not found, add it to the dictionary
        # return False

        # Time complexity: O(n) where n is the number of elements in the list
        # Space complexity: O(n) since we are storing the frequency of each element in the list

        # Set approach
        dup = set() # create a set to store the elements in the list
        for i in nums:
            if i in dup:
                return True
            else:
                dup.add(i) # add the element to the set if it is not in the set yet
        return False

        # Time complexity: O(n) where n is the number of elements in the list
        s# Space complexity: O(n) due to the storage of elements in the set


def main() -> None:
    nums1 = [1,2,3,1]
    # expected: True
    nums2 = [1,2,3,4]
    # expected: False
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    # expected: True
    sol = Solution()
    print(sol.containsDuplicate(nums1))
    print(sol.containsDuplicate(nums2))
    print(sol.containsDuplicate(nums3))

if __name__ == '__main__':
    main()