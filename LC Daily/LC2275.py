from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Initialize an array to count the number of '1's in each bit position
        # Since we assume numbers can be represented in 24 bits, we create a list with 24 zeros
        bit_count = [0] * 24

        for i in candidates:
            # For each bit position from 0 to 23, check if the bit at that position is '1' in the current number
            for j in range(24):
                # Right shift the number i by j positions, then check if the least significant bit is '1'
                # (i >> j) & 1 extracts the j-th bit of i.
                if (i >> j) & 1:
                    # If the j-th bit of i is 1, increment the count for that bit position
                    bit_count[j] += 1

        # The maximum value in bit_count gives the largest subset size with a non-zero bitwise AND
        return max(bit_count)

    # Time complexity: O(n * 24) = O(n), where n is the number of elements in the input list
    # We perform a constant amount of work (checking 24 bit positions) for each element
    # Space complexity: O(1), since we use a fixed size array of length 24 to store the bit counts


def main() -> None:
    candidates = [16,17,71,62,12,24,14]
    # expected: 4
    candidates1 = [8,8]
    # expected: 2
    candidates2 = [10000000,6777215]
    # expected: 1
    candidates3 = [10000000,8388608]
    # expected: 2
    sol = Solution()
    print(sol.largestCombination(candidates))
    print(sol.largestCombination(candidates1))
    print(sol.largestCombination(candidates2))
    print(sol.largestCombination(candidates3))

if __name__ == '__main__':
    main()