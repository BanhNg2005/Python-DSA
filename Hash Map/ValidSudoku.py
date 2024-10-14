from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create hash sets to store the values seen in each column, row, and 3x3 square
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key = (r // 3, c // 3)

        # Iterate over each cell in the 9x9 Sudoku board
        for r in range(9):
            for c in range(9):
                # Skip empty cells
                if board[r][c] == ".":
                    continue

                # Check if the current value is already in the current row, column, or 3x3 square
                if (
                        board[r][c] in rows[r]  # Check if the value is in the current row
                        or board[r][c] in cols[c]  # Check if the value is in the current column
                        or board[r][c] in squares[(r // 3, c // 3)]  # Check if the value is in the current 3x3 square
                ):
                    return False  # If the value is found in any of these, the board is invalid

                # Add the current value to the sets for the current row, column, and 3x3 square
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # If no duplicates are found, the board is valid
        return True

    # Time complexity: O(1) because we are iterating through a 9x9 board
    # and checking if the value is in the hash set which is a constant time operation (O(1))
    # Space complexity: O(1) because we are storing at most 9 values in each hash set
    # and there are 27 hash sets in total (9 rows, 9 columns, and 9 3x3 squares)

# For visual representation for the squares hash set:

# (0,0) (0,0) (0,0) | (0,1) (0,1) (0,1) | (0,2) (0,2) (0,2)
# (0,0) (0,0) (0,0) | (0,1) (0,1) (0,1) | (0,2) (0,2) (0,2)
# (0,0) (0,0) (0,0) | (0,1) (0,1) (0,1) | (0,2) (0,2) (0,2)
# ------------------+-------------------+------------------
# (1,0) (1,0) (1,0) | (1,1) (1,1) (1,1) | (1,2) (1,2) (1,2)
# (1,0) (1,0) (1,0) | (1,1) (1,1) (1,1) | (1,2) (1,2) (1,2)
# (1,0) (1,0) (1,0) | (1,1) (1,1) (1,1) | (1,2) (1,2) (1,2)
# ------------------+-------------------+------------------
# (2,0) (2,0) (2,0) | (2,1) (2,1) (2,1) | (2,2) (2,2) (2,2)
# (2,0) (2,0) (2,0) | (2,1) (2,1) (2,1) | (2,2) (2,2) (2,2)
# (2,0) (2,0) (2,0) | (2,1) (2,1) (2,1) | (2,2) (2,2) (2,2)

def main() -> None:
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    # expected: True
    invalid_board = \
        [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # expected: False
    sol = Solution()
    print(sol.isValidSudoku(board))
    print(sol.isValidSudoku(invalid_board))


if __name__ == '__main__':
    main()