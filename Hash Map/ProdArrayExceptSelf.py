from typing import List

# idea: create two lists, one for the left product and one for the right product
# multiply the left product with the right product to get the final product
# by adding 1 to the left multiplier and right multiplier for the first element of each list
# example: [1, 2, 3, 4]
# left product:  [1, 1, 2, 6] no need to multiply the last element since we will go out of bounds
# right product: [24, 12, 4, 1]
# final product: [24, 12, 8, 6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1 # add 1 to the left multiplier for the first element of left product
        r_mult = 1 # add 1 to the right multiplier for the first element of right product
        n = len(nums) 
        l_array = [0] * n # create a list of n zeros for the left product
        r_array = [0] * n # create a list of n zeros for the right product

        for i in range(n):
            j = -i - 1 
            # j is going backwards from the end of the list to the beginning of the right product
            # as i move to the right, j moves to the left to make sure they will not go out of bounds
            l_array[i] = l_mult
            r_array[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        
        return [l_array[i] * r_array[i] for i in range(n)]
    
    # Time complexity: O(n) where n is the number of elements in the list
    # Space complexity: O(n) since we are storing the left and right product in two separate lists

def main() -> None:
    nums = [1, 2, 3, 4] 
    
    # expected: [24, 12, 8, 6]
    sol = Solution()
    print(sol.productExceptSelf(nums))

if __name__ == '__main__':
    main()