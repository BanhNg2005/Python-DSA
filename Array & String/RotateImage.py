from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) # Get the number of rows (or columns, since the matrix is square)

        # Step 1: Transpose the matrix
        # Transposing means converting rows to columns and vice versa
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        # This will effectively rotate the matrix by 90 degrees
        for i in range(n):
            for j in range(n // 2): # We only need to go halfway to reverse the row
                # n - j - 1 is the index of the element on the opposite side of the row from the current element
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1],  matrix[i][j]

        # Time complexity: O(n^2) where n is the number of rows (or columns) in the matrix
        # Space complexity: O(1) since we are not using any extra space

def main() -> None:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix3 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    sol = Solution()
    sol.rotate(matrix)
    sol.rotate(matrix2)
    sol.rotate(matrix3)
    print(matrix)
    print(matrix2)
    print(matrix3)

if __name__ == '__main__':
    main()