from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])  # number of rows and columns
        result = []
        i, j = 0, 0
        Up, Right, Down, Left = 0, 1, 2, 3 # 0, 1, 2, 3 represent the direction

        direction = Right
        upWall = 0
        rightWall = n
        downWall = m
        leftWall = -1

        while len(result) != m * n: # loop until the result list is filled with all the elements
            if direction == Right:
                while j < rightWall: # loop until the right wall is reached
                    # appends the current element of the matrix, located at row i and column j, to the result list.
                    result.append(matrix[i][j])
                    j += 1 # continue to move to the right until the right wall is reached
                i, j = i + 1, j - 1 # go to the next row and move back one column (avoid going out of bounds)
                rightWall -= 1 # go back one column to avoid going out of bounds
                direction = Down
            elif direction == Down:
                while i < downWall:
                    result.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1 # go back one row and move back one column (avoid going out of bounds) as we move up
                downWall -= 1
                direction = Left
            elif direction == Left:
                while j > leftWall:
                    result.append(matrix[i][j])
                    j -= 1
                i, j = i - 1, j + 1 # go back one row and move one column to the right (avoid going out of bounds)
                leftWall += 1
                direction = Up
            elif direction == Up:
                while i > upWall:
                    result.append(matrix[i][j])
                    i -= 1 # move up until the up wall is reached
                i, j = i + 1, j + 1 # go back one row and move one column to the right (avoid going out of bounds)
                upWall += 1
                direction = Right
        return result
        # Time complexity: O(m*n) where m is the number of rows and n is the number of columns
        # Space complexity: O(1) since we store everything in the result list

def main() -> None:
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
    sol = Solution()
    print(sol.spiralOrder(matrix1))
    print(sol.spiralOrder(matrix2))
    print(sol.spiralOrder(matrix3))

if __name__ == '__main__':
    main()