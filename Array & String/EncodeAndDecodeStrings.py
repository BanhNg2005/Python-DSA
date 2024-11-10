from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return result

    # Time complexity: O(n) where n is the total number of characters in the list of words
    # Space complexity: O(n) since we are storing the encoded string

def main() -> None:
    strs = ["hello", "world"]
    sol = Solution()
    encoded_str = sol.encode(strs)
    print("Encoded:", encoded_str)
    decoded_list = sol.decode(encoded_str)
    print("Decoded:", decoded_list)

if __name__ == '__main__':
    main()