from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        l = 0
        curr_sum = 0

        for r in range(n + abs(k)):  # Ensure the window covers the necessary elements
            curr_sum += code[r % n]  # Add the element at the right boundary

            if r - l + 1 > abs(k):  # If the window size exceeds k
                curr_sum -= code[l % n]  # Subtract the element at the left boundary
                l = (l + 1) % n  # Move the left boundary to the right

            if r - l + 1 == abs(k):  # When the window size equals k
                if k > 0:
                    result[(l - 1) % n] = curr_sum  # update the sum to the appropriate position
                elif k < 0:
                    result[(r + 1) % n] = curr_sum  # same as above but for negative k so we need to move the right boundary

        return result

    # Time complexity: O(n)
    # Space complexity: O(n)

def main() -> None:
    code = [5,7,1,4]
    k = 3
    # expected: [12,10,16,13]
    code1 = [1,2,3,4]
    k1 = 0
    # expected: [0,0,0,0]
    code2 = [2,4,9,3]
    k2 = -2
    # expected: [12,5,6,13]
    sol = Solution()
    print(sol.decrypt(code, k))
    print(sol.decrypt(code1, k1))
    print(sol.decrypt(code2, k2))

if __name__ == '__main__':
    main()