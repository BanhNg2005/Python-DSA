from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:  # in case of duplicates, we skip; and i > 0 to make sure they are in bounds
                continue

            low, high = i + 1, n - 1
            while low < high:
                summ = nums[i] + nums[low] + nums[high]
                if summ == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    low, high = low + 1, high - 1
                    while low < high and nums[low] == nums[low - 1]: # make sure low is in bounds and we don't want two consecutive duplicates
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif summ < 0:
                    low += 1
                else:
                    high -= 1
        return res

    # Time complexity: O(n^2) because we loop through the list and also loop through the 2 pointers low and high
    # Space complexity: O(1) because we don't take any extra space

def main() -> None:
    nums = [-1,0,1,2,-1,-4]
    # expected: [[-1,-1,2],[-1,0,1]]
    nums1 = [3, 2, 2, 0, 1, -3, -2, -3, -1]
    # expected: [[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2]]
    sol = Solution()
    print(sol.threeSum(nums))
    print(sol.threeSum(nums1))

if __name__ == '__main__':
    main()