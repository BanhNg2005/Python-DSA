from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:
            if i == '+':
                stack.append(stack[-1] + stack[-2]) # we want to sum the last two integers in the stack
            elif i == 'D':
                stack.append(stack[-1] * 2) # we want to double the last integer in the stack
            elif i == 'C':
                stack.pop() # we want to remove the last integer in the stack
            else:
                stack.append(int(i)) # just simply append the integer to the stack
        return sum(stack)

    # Time complexity: O(n) because we iterate through the list
    # Space complexity: O(n) because we store the elements in the stack

def main() -> None:
    op = ["5","2","C","D","+"]
    # expected: 30
    op1 = ["5","-2","4","C","D","9","+","+"]
    # expected: 27
    sol = Solution()
    print(sol.calPoints(op))
    print(sol.calPoints(op1))

if __name__ == '__main__':
    main()