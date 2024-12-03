from typing import List

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i, j = 0, 0 # pointer on the string and the other on the spaces (we care the value of space at the position j)
        result = []

        while i < len(s) and j < len(spaces):
            if i < spaces[j]:
                result.append(s[i])
                i += 1
            else:
                result.append(" ")
                j += 1

        # in case we go through all the spaces
        if i < len(s):
            result.append(s[i:]) # add all the char start at s to the end of the string

        return "".join(result)

        # Time: O(n)
        # Space: O(n)

def main() -> None:
    s = "icodeinpython"
    spaces = [1,5,7,9]
    # expected: "i code in python"
    s1 = "spacing"
    spaces1 = [1, 2, 3, 4, 5, 6]
    # expected: "s p a c i n g"
    sol = Solution()
    print(sol.addSpaces(s, spaces))
    print(sol.addSpaces(s1, spaces1))

if __name__ == '__main__':
    main()