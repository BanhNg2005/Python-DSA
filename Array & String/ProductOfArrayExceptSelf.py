from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums)) # create a result output array and we want the length of the array to be the same as the input array

        prefix = 1

        for i in range(len(nums)): # go through every position in the array
            result[i] = prefix # just take the prefix and put it in the position i
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1): # start from the end of the array and go backwards
            result[i] *= postfix
            postfix *= nums[i]

        return result
