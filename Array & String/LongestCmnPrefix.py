from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sorted_strs = sorted(strs) # sort the strings in lexicographical order
        prefix = ''
        for i in range(len(sorted_strs[0])):
            if sorted_strs[0][i] == sorted_strs[-1][i]: # if the first and last string have the same character at the ith index
                prefix += sorted_strs[0][i] # add the character to the prefix
        return prefix

        # Time complexity: O(nlogn) where n is the length of the longest string in the list
        # Space complexity: O(1)


def main() -> None:
    strs = ['crunchy', 'cramp', 'crying']
    sol = Solution()
    print(sol.longestCommonPrefix(strs))

if __name__ == '__main__':
    main()

