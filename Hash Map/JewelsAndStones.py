class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        # brute force method
        # counter = 0

        # for i in stones:
        #     if i in jewels:
        #         counter += 1
        # return counter
        # Time complexity: O(n * m) where n is the length of jewels and m is the length of stones
        # Space complexity: O(1) because we are not using any extra space

        ##########################################################################

        # hash set method

        s = set(jewels) # ('a', 'A')
        counter = 0
        for i in stones:
            if i in s:
                counter += 1

        return counter

    # hash set is slightly faster than hash map because it doesn't have to store a value
    # hash set is slower in small input compared to brute force method, yet faster in large input

    # Time complexity: O(n + m) or O(1) where n is the length of jewels and m is the length of stones
    # Space complexity: O(n) where n is the length of jewels

def main() -> None:
    jewels1 = 'aA'
    stones1 = 'aAAbbbb'
    # expected: 3
    jewels2 = 'z'
    stones2 = 'ZZ'
    # expected: 0
    sol = Solution()
    print(sol.numJewelsInStones(jewels1, stones1))
    print(sol.numJewelsInStones(jewels2, stones2))

if __name__ == '__main__':
    main()