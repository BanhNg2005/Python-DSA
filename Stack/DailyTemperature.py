from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n = len(temperatures)
        # stk = []
        # result = [0] * n
        # for i in range(n):
        #     while stk and temperatures[i] > temperatures[stk[-1]]:
        #         index = stk.pop()
        #         result[index] = i - index
        #     stk.append(i)
        # return result

        # Another way to do it
        n = len(temperatures)
        result = [0] * n
        stk = []

        for i, t in enumerate(temperatures):
            while stk and stk[-1][0] < t: # `stk[-1][0]` is the temperature of the last element in the stack `stk`
                # we store the temperature and index of the last element in the stack `stk` and pop it out of the stack
                stk_t, stk_i = stk.pop()
                result[stk_i] = i - stk_i
            stk.append((t, i))
        return result

        # Time: O(n)
        # Space: O(n) because we just put everything in the stack

def main() -> None:
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    # expected: [1, 1, 4, 2, 1, 1, 0, 0]
    sol = Solution()
    print(sol.dailyTemperatures(temps))

if __name__ == '__main__':
    main()