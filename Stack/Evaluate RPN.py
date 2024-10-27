from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i not in "+-*/":
                stk.append(int(i))
            else:
                # we want to pop the last two elements in the stack
                # and perform the operation on them
                # we name 'a' as the first element and 'b' as the second element
                # because the order matters for subtraction and division
                b, a = stk.pop(), stk.pop()
                if i == '+':
                    stk.append(a + b)
                elif i == '-':
                    stk.append(a - b)
                elif i == '*':
                    stk.append(a * b)
                else:
                    stk.append(int(a / b))
        return stk[0] # we return the only element left in the stack

    # Time complexity: O(n) because we go through the length n of tokens
    # Space complexity: O(n) because we store the elements in the stack

def main() -> None:
    tokens = ["2", "1", "+", "3", "*"]
    # expected: 9
    tokens1 = ["4", "13", "5", "/", "+"]
    # expected: 6
    tokens2 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    # expected: 22
    sol = Solution()
    print(sol.evalRPN(tokens))
    print(sol.evalRPN(tokens1))
    print(sol.evalRPN(tokens2))

if __name__ == '__main__':
    main()