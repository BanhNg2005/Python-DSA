from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sorted_strs = sorted(strs) # sort the strings in lexicographical order
        # prefix = ''
        # for i in range(len(sorted_strs[0])):
        #     if sorted_strs[0][i] == sorted_strs[-1][i]: # if the first and last string have the same character at the ith index
        #         prefix += sorted_strs[0][i] # add the character to the prefix
        # return prefix

        # Time complexity: O(nlogn) where n is the length of the longest string in the list
        # Space complexity: O(1)

        min_length = float('inf') # make sure we don't go out of bounds when comparing strings

        for s in strs:
            if len(s) < min_length: # find the length of the shortest string
                min_length = len(s) # update the length of the shortest string

        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]: # check if each string has the same character at the ith index
                    return s[:i] # return the prefix up to the ith index
            i += 1 # increment the index

        return s[:i] # force us to return no matter what (if there is an empty string in the list, return an empty string)
        # Time: O(n * m) where n is the number of strings and m is the length of the shortest string
        # Space: O(1) since we are not using any extra space


def main() -> None:
    strs = ['crunchy', 'cramp', 'crying']
    sol = Solution()
    print(sol.longestCommonPrefix(strs))

if __name__ == '__main__':
    main()

