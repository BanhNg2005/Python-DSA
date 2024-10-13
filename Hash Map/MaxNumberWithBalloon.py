from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = "balloon"

        for i in text:
            if i in balloon: # constant time operation
                counter[i] += 1 # add frequency for char i in text that is in balloon

        if any( i not in counter for i in balloon): # check if any of the letters in balloon are not in the text
            return 0
        else:
            # constant time operation
            return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])
            # // 2 because we need two 'l's and two 'o's to form the word balloon

        # Time complexity: O(n) where we iterate through the text
        # Space complexity: O(1) because we are forcing to store the frequency of the letters in the balloon word

def main() -> None:
    text = "nlaebolko"
    # expected: 1
    text1 = "loonbalxballpoon"
    # expected: 2
    text2 = "leetcode"
    # expected: 0
    sol = Solution()
    print(sol.maxNumberOfBalloons(text))
    print(sol.maxNumberOfBalloons(text1))
    print(sol.maxNumberOfBalloons(text2))

if __name__ == '__main__':
    main()