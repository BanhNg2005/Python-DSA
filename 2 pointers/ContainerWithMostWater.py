from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_area = 0

        while left < right: # we need to make sure that the pointers don't overlap
            w = right - left # width of the container
            h = min(height[left], height[right]) # we cannot exceed the height of the shorter line
            a = h * w
            max_area = max(max_area, a) # update the max_area if the current area is greater
            if height[left] < height[right]: # if shorter, we move the left pointer to the right to see if we can get a greater area
                left += 1
            else:
                right -= 1
        return max_area

    # Time complexity: O(n) because we are just moving the pointers left or right once
    # Space complexity: O(1) since we just have one variable max_area to store the maximum area

def main() -> None:
    height = [1,8,6,2,5,4,8,3,7]
    # expected: 49
    height1 = [1,1]
    # expected: 1
    height2 = [4,3,2,1,4]
    # expected: 16
    height3 = [1,2,1]
    # expected: 2
    sol = Solution()
    print(sol.maxArea(height))
    print(sol.maxArea(height1))
    print(sol.maxArea(height2))
    print(sol.maxArea(height3))

if __name__ == '__main__':
    main()