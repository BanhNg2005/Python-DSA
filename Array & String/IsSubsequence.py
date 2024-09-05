class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        A, B = len(s), len(t)

        if A > B:
            return False
        i, j = 0, 0

        while i < A and j < B: # while we haven't reached the end of s and t
            if s[i] == t[j]:
                i += 1  # move to the next character in s
            j += 1  # always move to the next character in t

        return i == A  # if matched all characters of s
        # Time: O(n) where n is the length of the string
        # Space: O(1) because we only use 2 variables i and j





def main() -> None:
    s = 'abc'
    t = 'ahbgdc'
    solution = Solution()
    print(solution.isSubsequence(s, t))

if __name__ == '__main__':
    main()