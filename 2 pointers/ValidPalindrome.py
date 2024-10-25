class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1

        while l < r:
            if not s[l].isalnum(): # we want to ignore any non-alphanumeric characters
                l += 1
                continue

            if not s[r].isalnum(): # same but for the right pointer
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True

    # Time complexity: O(n) because we are moving the pointers left or right which is just O(2n)
    # Space complexity: O(1) because we are just using the pointers l and r

def main() -> None:
    s1 = ".a"
    # expected: True
    s2 = "0P"
    # expected: False
    s3 = " "
    # expected: True
    sol = Solution()
    print(sol.isPalindrome(s1))
    print(sol.isPalindrome(s2))
    print(sol.isPalindrome(s3))

if __name__ == '__main__':
    main()