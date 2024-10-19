from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

def main() -> None:
    s = ["h","e","l","l","o"]
    # expected: ["o","l","l","e","h"]
    s1 = ["H","a","n","n","a","h"]
    # expected: ["h","a","n","n","a","H"]
    sol = Solution()
    sol.reverseString(s)
    sol.reverseString(s1)
    print(s)
    print(s1)

if __name__ == '__main__':
    main()