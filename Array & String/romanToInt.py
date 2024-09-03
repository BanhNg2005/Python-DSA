class Solution:
    def romanToInt(self, s: str) -> int:
        a: dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        tong = 0
        n = len(s) # length of the string
        i = 0 # index i at 0
        while i < n:
            # if i is less than the last index and the value of the letter at i is less than the value of the letter at i+1
            if i < n - 1 and a[s[i]] < a[s[i+1]]:
                # the greater value from the index i+1 minus the value of the letter at i and add it to the sum
                tong += a[s[i+1]] - a[s[i]]
                i += 2 # jump 2 indexes as we already used the value of the letter at i+1
            else:
                tong += a[s[i]] # just add the value i to the sum
                i += 1 # move to the next index

        return tong 
        # Time: O(n) where n is the length of the string
        # Space: O(1)

# Test
def main() -> None:
    s = 'MCMXCIV'
    sol = Solution()
    print(sol.romanToInt(s))

if __name__ == '__main__':
    main()