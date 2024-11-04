from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        max_left = [0] * n # create a list of n elements with all elements initialized to 0
        max_right = [0] * n
        for i in range(n):
            j = -i - 1 # start from the end of the list
            max_left[i] = l_wall # set the left wall to the current left wall
            max_right[j] = r_wall # set the right wall to the current right wall
            l_wall = max(l_wall, height[i]) # update the left wall
            r_wall = max(r_wall, height[j]) # update the right wall

        summ = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i]) # the potential water level is the minimum of the left and right walls
            summ += max(0, pot - height[i]) # the amount of water that can be trapped is the difference between the potential water level and the current height

        return summ

    # Time complexity: O(n) because we try to find the maximum height of the left and right walls for each element in the list
    # Space complexity: O(n) because we are creating two lists of n elements

def main() -> None:
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # expected: 6
    height1 = [11,679]
    # expected: 0
    height2 = [766,576,765]
    # expected: 189
    sol = Solution()
    print(sol.trap(height))
    print(sol.trap(height1))
    print(sol.trap(height2))

if __name__ == '__main__':
    main()