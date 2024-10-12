from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(int)

        for i in magazine:
            counter[i] += 1 # if found, increment the frequency of the letter
            # by using defaultdict, we don't have to check if the key is in the dictionary or not

        for i in ransomNote:
            if i not in counter: # if the letter is not found in the magazine, return False
                return False
            elif counter[i] == 1: # if the letter is found and the frequency is 1, delete the key
                del counter[i]
            else:
                counter[i] -= 1 # if the letter is found and the frequency is greater than 1, decrement the frequency
        return True
        # Purpose of the second loop is to check if the ransomNote can be constructed from the magazine
        # if there is nothing left in the counter dictionary, return True

    # Time complexity: O(n + m) where n is the length of ransomNote and m is the length of magazine
    # Space complexity: O(m) where m is where we are storing the frequency of each letter in the magazine
    
def main() -> None:
    ransomNote = "aa"
    magazine = "aab"
    # expected: True
    ransomNote1 = "fihjjjjei"
    magazine1 = "hjibagacbhadfaefdjaeaebgi"
    # expected: False
    sol = Solution()
    print(sol.canConstruct(ransomNote, magazine))
    print(sol.canConstruct(ransomNote1, magazine1))

if __name__ == '__main__':
    main()