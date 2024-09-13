from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        n = len(nums)
        l_array = [0] * n
        r_array = [0] * n

        for i in range(n):
            j = -i - 1
            l_array[i] = l_mult
            r_array[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        
        return [l_array[i] * r_array[i] for i in range(n)]
    
    # Time complexity: O(n) where n is the number of elements in the list
    # Space complexity: O(n) where n is the number of elements in the list

def main() -> None:
    nums = [1, 2, 3, 4]
    # expected: [24, 12, 8, 6]
    sol = Solution()
    print(sol.productExceptSelf(nums))

if __name__ == '__main__':
    main()