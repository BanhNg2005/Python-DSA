from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 3 rules
        # only add parenthesis if the open parenthesis < n
        # only add a closing parenthesis if closed < open
        # stop the count once open == closed == n

        stack = []
        result = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return result

def main() -> None:
    n = 3
    # expected: ["((()))","(()())","(())()","()(())","()()()"]
    n1 = 1
    # expected: ["()"]
    n2 = 2
    # expected: ["(())","()()"]
    sol = Solution()
    print(sol.generateParenthesis(n))
    print(sol.generateParenthesis(n1))
    print(sol.generateParenthesis(n2))

if __name__ == '__main__':
    main()