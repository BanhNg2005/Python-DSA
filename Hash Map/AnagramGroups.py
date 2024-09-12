from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list) # mapping character count to list of anagrams

        for s in strs: # go through every string that we're given
            count = [0] * 26 # count each of the letter from a to z (or creating 26 0 in the list)

            for c in s: # each char c in the current string s
                count[ord(c) - ord("a")] += 1 # compute the index for character c and increment the count at that index
                # the letter will be converted to an ascii value and if the letter is found
                # the index in the count list (which is 26 zeros) will be added and increment by 1

            h[tuple(count)].append(s)
            # use the count list as the key (converted to a tuple)
            # and append the original string (s) to the list of anagrams

        return h.values() # return all the grouped anagram




def main() -> None:
    strs = ["act","pots","tops","cat","stop","hat"]
    # expected: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    sol = Solution()
    print(sol.groupAnagrams(strs))

if __name__ == '__main__':
    main()
